import secrets # To use random generator for numbers

class Playlist:
	
	# Create noteNumber and playlist members
	# noteNumber is the reference tone
	# maxNote is the maximum playable note on the instrument
	def __init__(self, noteNumber, maxNote):
		self.noteNumber = noteNumber
		self.maxNote = maxNote
		self.playlist = []
		self.soundSet = set()
		self.addToSoundSet(0) # This chooses mode of operation
		self.addStrings()
		self.randomize()

	# Get the last element in the list by popping it
	# The noteNumber is appended to the list before returning it
	# This allows the ability to change reference tone
	def getNextSound(self):
		sound = self.playlist.pop()
		sound.append(self.noteNumber)
		return sound

	# Randomize sounds in playlist to avoid predictability
	def randomize(self):
		for i in range(len(self.playlist)):
			randomIndex = secrets.randbelow(len(self.playlist))
			temp = self.playlist[i]
			self.playlist[i] = self.playlist[randomIndex]
			self.playlist[randomIndex] = temp

	# Reset playlist to an empty list
	def resetPlaylist(self):
		self.playlist = []

	# Print the reference note for the playlist
	def printReferenceNote(self):
		print(self.noteNumber)

	# Print the max note for the playlist
	def printMaxNote(self):
		print(self.maxNote)

	# Print sounds inside the playlist
	def printSounds(self):
		for s in self.playlist:
			print(s)

	# Add the allowed sounds to a hashset depending on mode
	# Do NOT confuse these modes with musical modes! These are only modes of operation
	# This allows for different modes (licks, triads, scales, etc.)
	# Mode 0: Reserved for on-demand sounds (such as to pinpoint weak areas)
	# Mode 1: All the sounds
	# Mode 2: Scales
	# Mode 3: Triads and Chords (including 7ths, 9ths)
	# Mode 4: Licks
	def addToSoundSet(self, mode):
		if (mode == 0):
			self.soundSet = {9}
		if (mode == 1):
			self.soundSet = {0, 1, 2, 3}


	# Add strings containing name to playlist based on reference note
	# A sound must be contained in hashset in order to be added
	# List Format is [MIDI_FILE_NAME, START_STEP, CORRECTION, TRIM_DURATION_MS]
	# UNFORTUNATELY PRETTY MUCH HARDCODED LOGIC :(((
	def addStrings(self):

		if self.noteNumber >= 21:
			if 2 in self.soundSet: self.playlist.append(['2', -9, -12, 3400])

		if self.noteNumber >= 12:
			if 0 in self.soundSet: self.playlist.append(['0', 0, -12, 5000])

		if self.noteNumber >= 9:
			if 2 in self.soundSet: self.playlist.append(['2', -9, 0, 3400]) # REFERENCE 2

		if self.noteNumber >= 4:
			if 1 in self.soundSet: self.playlist.append(['1', 0, -4, 2700])

		if self.noteNumber >= 3:
			if self.noteNumber <= self.maxNote - 9:
				if 0 in self.soundSet: self.playlist.append(['0', 0, -3, 5000])

		# 

		if self.noteNumber <= self.maxNote - 4:
			if 1 in self.soundSet: self.playlist.append(['1', 0, 0, 2700]) # REFERENCE 1

		if self.noteNumber <= self.maxNote - 7:
			if 9 in self.soundSet: self.playlist.append(['9', 0, 0, 3400]) # REFERENCE 9

		if self.noteNumber <= self.maxNote - 8:
			if 1 in self.soundSet: self.playlist.append(['1', 0, +4, 2700])

		if self.noteNumber <= self.maxNote - 12:
			if 0 in self.soundSet: self.playlist.append(['0', 0, 0, 5000]) # REFERENCE 0
			if 3 in self.soundSet: self.playlist.append(['3', 0, 0, 5600]) # REFERENCE 3

		if self.noteNumber <= self.maxNote - 17:
			if 3 in self.soundSet: self.playlist.append(['3', 0, +5, 5600])