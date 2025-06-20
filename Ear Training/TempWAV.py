import mido
import os
import subprocess
from mido import MetaMessage, bpm2tempo
from tempfile import NamedTemporaryFile
from pydub import AudioSegment

class TempWAVfile:
    # Constructor that transposes and creates WAV file
    # List Format is [MIDI_FILE_NAME, START_STEP, CORRECTION, TRIM_DURATION_MS, NUM_STEPS]
    # START_STEP is the first note in the soundfile?
    # NUM_STEPS is the number of steps to be transposed
    # TRIM_DURATION_MS is the duration of .WAV file in milliseconds
    def __init__(self, sound):
        INPUT_MIDI = 'Sounds/Starting MIDI Files/'+sound[0]+'.mid'
        original_midi = mido.MidiFile(INPUT_MIDI)
        OUTPUT_DIR = 'Sounds/'
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        wav_out = os.path.join(OUTPUT_DIR, 'Temp.wav')
        self.render_transposed_wav(original_midi, 0-sound[1]+sound[2]+sound[4], wav_out, sound[3])

    # Transpose the MIDI file by the desired number of steps
    def transpose_midi_in_memory(self, mid, semitone_shift, tempo_bpm):
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

    # Render the Temp WAV file from the transposed MIDI file
    def render_transposed_wav(self, original_mid, semitone_shift, output_wav_path, trim_duration):
        TEMPO_BPM = 120 # [JUST LEAVE THIS AS IS]
        transposed_mid = self.transpose_midi_in_memory(original_mid, semitone_shift, TEMPO_BPM)

        # Save transposed MIDI to temp file
        with NamedTemporaryFile(suffix='.mid', delete=False) as temp_midi:
            transposed_mid.save(temp_midi.name)
            temp_midi_path = temp_midi.name

        # Timidity options: disable reverb/chorus and boost gain
        # All output will be suppressed
        with open(os.devnull, 'w') as devnull:
            subprocess.run([
                'timidity',
                temp_midi_path,
                '-Ow', # Output WAV
                '-o', output_wav_path,
                '-A', '600', # Amplify to percentage
                '-EFreverb=0' # No Reverb
                ], stdout=devnull, stderr=devnull, check=True)

        os.remove(temp_midi_path)

        # Trim silence
        self.trim_wav(output_wav_path, trim_duration)

    # Trims the file to the specified millisecond duration
    def trim_wav(self, wav_path, max_duration_ms):
        audio = AudioSegment.from_wav(wav_path)
        trimmed = audio[:max_duration_ms]
        trimmed.export(wav_path, format="wav")