from mido import Message, MidiFile, MidiTrack, MetaMessage
import math

def semitone_to_pitchwheel(semitone, range_semitones=2):
    """Convert semitone offset to pitchwheel value in range -8192..8191."""
    return int((semitone / range_semitones) * 8191)

def ease_in(step, total):
    """Ease-in curve (slow to fast)"""
    return math.pow(step / total, 2)

# Create MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo (120 BPM)
track.append(MetaMessage('set_tempo', tempo=500000))

# Optional: set pitch bend range to ±2 semitones (default for most synths)
track.extend([
    Message('control_change', control=101, value=0),  # RPN MSB
    Message('control_change', control=100, value=0),  # RPN LSB
    Message('control_change', control=6, value=2),    # Pitch bend range = 2 semitones
    Message('control_change', control=38, value=0),   # Cents
])

# Parameters
note = 60  # Middle C
velocity = 100
bend_target_semitone = 1
bend_steps = 50
step_duration = 5  # ticks
note_duration = bend_steps * step_duration + 240  # holds after bend

# Start note
track.append(Message('note_on', note=note, velocity=velocity, time=0))

# Gradually bend pitch up using an ease-in curve
for step in range(1, bend_steps + 1):
    ratio = ease_in(step, bend_steps)
    pitch = semitone_to_pitchwheel(bend_target_semitone * ratio)
    track.append(Message('pitchwheel', pitch=pitch, time=step_duration))

# Hold final bent note
track.append(Message('note_off', note=note, velocity=0, time=240))

# Save file
filename = "one_note_bend_up.mid"
mid.save(filename)
print(f"Saved: {filename}")
