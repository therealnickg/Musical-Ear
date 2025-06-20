import mido
import os
import subprocess
from mido import MetaMessage, bpm2tempo
from tempfile import NamedTemporaryFile
from pydub import AudioSegment

# === CONFIG ===
MIDI_FILE_NAME = '4'
INPUT_MIDI = 'Sounds/Starting MIDI Files/'+MIDI_FILE_NAME+'.mid'
OUTPUT_DIR = 'Exported WAVs'
NUM_STEPS = 39 # Number of times to be transposed
TRIM_DURATION_MS = 2700 # Milliseconds duration of .WAV file
STEP_INCREASE = 0 # What is the first note in the soundfile?
TEMPO_BPM = 120 # [JUST LEAVE THIS AS IS]

os.makedirs(OUTPUT_DIR, exist_ok=True)

def transpose_midi_in_memory(mid, semitone_shift, tempo_bpm):
    new_mid = mido.MidiFile(ticks_per_beat=mid.ticks_per_beat)

    for i, track in enumerate(mid.tracks):
        new_track = mido.MidiTrack()
        if i == 0:
            # Add tempo at the beginning of the first track
            new_track.append(MetaMessage('set_tempo', tempo=bpm2tempo(tempo_bpm), time=0))
        for msg in track:
            if msg.type in ('note_on', 'note_off'):
                new_note = max(0, min(127, msg.note + semitone_shift))
                new_msg = msg.copy(note=new_note)
                new_track.append(new_msg)
            else:
                new_track.append(msg)
        new_mid.tracks.append(new_track)

    return new_mid

def render_transposed_wav(original_mid, semitone_shift, output_wav_path):
    transposed_mid = transpose_midi_in_memory(original_mid, semitone_shift, TEMPO_BPM)

    # Save transposed MIDI to temp file
    with NamedTemporaryFile(suffix='.mid', delete=False) as temp_midi:
        transposed_mid.save(temp_midi.name)
        temp_midi_path = temp_midi.name

    # Timidity options: disable reverb/chorus and boost gain
    cmd = [
        'timidity',
        temp_midi_path,
        '-Ow', # Output WAV
        '-o', output_wav_path,
        '-A', '600', # Amplify to percentage
        '-EFreverb=0' # No Reverb
    ]

    subprocess.run(cmd, check=True)
    os.remove(temp_midi_path)

    # Trim silence
    trim_wav(output_wav_path, TRIM_DURATION_MS)

def trim_wav(wav_path, max_duration_ms):
    audio = AudioSegment.from_wav(wav_path)
    trimmed = audio[:max_duration_ms]
    trimmed.export(wav_path, format="wav")

# === Main Processing ===
original_midi = mido.MidiFile(INPUT_MIDI)

print(f"Generating {NUM_STEPS} WAVs with transpositions...")

for step in range(NUM_STEPS + 1):
    wav_out = os.path.join(OUTPUT_DIR, MIDI_FILE_NAME+f'_{step+STEP_INCREASE}.wav')
    print(f"  ➜ +{step} semitones -> {wav_out}")
    render_transposed_wav(original_midi, step, wav_out)

print("All Done. WAVs saved to:", OUTPUT_DIR)
