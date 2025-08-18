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
		self.playlist.append(['0', 0, 0, 3]) # DUMMY NODE (Values not important)

	# Get the last element in the list by popping it
	# The noteNumber is appended to the list before returning it
	# This allows the ability to change reference tone
	def getNextSound(self):
		sound = self.playlist.pop()
		sound.append(self.noteNumber)
		return sound

	# Randomize sounds in playlist to avoid predictability by using for loop
	def randomize(self):
		for i in range(len(self.playlist)):
			randomIndex = secrets.randbelow(len(self.playlist))
			temp = self.playlist[i]
			self.playlist[i] = self.playlist[randomIndex]
			self.playlist[randomIndex] = temp

	# Return length of current list
	def lengthPlaylist(self):
		return len(self.playlist)

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

	# Add the allowed sounds to a hashset depending on mode of operation
	# Do NOT confuse these "modes" with musical modes! These are only modes of operation
	# This allows for different modes (licks, triads, scales, etc.)
	def addToSoundSet(self, mode):
		# Mode 0: Reserved for on-demand sounds (such as to pinpoint weak areas)
		if (mode == 0):
			self.soundSet.update({0})
		# Mode 1: All the sounds
		if (mode == 1):
			self.soundSet.update({0, 1, 2, 3, 4, 9, 11, 12, 13})
		# Mode 2: Scales (Major, Minor, Pentatonic, Harmonic, Modes, etc.)
		if (mode == 2):
			self.soundSet.update({0, 3, 5, 6, 11, 12, 13})
		# Mode 3: Triads, Chords, Arpeggios (including 7ths, 9ths, Diminished, Half-Diminished)
		if (mode == 3):
			self.soundSet.update({4, 8})
		# Mode 4: Licks and Melodies
		if (mode == 4):
			self.soundSet.update({1, 2, 7, 9, 10})
		# Do we want to exclude any sounds? Sounds in the set below will be exluded.
		# Set should be empty by default
		self.soundSet.difference_update({})


	# Add strings containing name to playlist based on reference note
	# A sound must be contained in hashset in order to be added
	# List Format is [MIDI_FILE_NAME, CORRECTION, TRIM_DURATION_MS]
	# UNFORTUNATELY PRETTY MUCH HARDCODED LOGIC :(((
	def addStrings(self):

		if self.noteNumber >= 14:
			if self.noteNumber <= self.maxNote - 5:
				if 2 in self.soundSet: self.playlist.append(['2', -9, -5, 3400])

		if self.noteNumber >= 12:
			if 0 in self.soundSet: self.playlist.append(['0', 0, -12, 5000])
			if 3 in self.soundSet: self.playlist.append(['3', 0, -12, 5600])
			if 12 in self.soundSet: self.playlist.append(['12', 0, -12, 5000])
			if 11 in self.soundSet: self.playlist.append(['11', 0, -12, 5000])
			if 13 in self.soundSet: self.playlist.append(['13', 0, -12, 5600])

		if self.noteNumber >= 9:
			if 2 in self.soundSet: self.playlist.append(['2', -9, 0, 3400]) # REFERENCE 2

		if self.noteNumber >= 7:
			if 4 in self.soundSet: self.playlist.append(['4', 0, -7, 2700])

		if self.noteNumber >= 4:
			if 1 in self.soundSet: self.playlist.append(['1', 0, -4, 2700])
			if 4 in self.soundSet: self.playlist.append(['4', 0, -4, 2700])

		if self.noteNumber >= 3:
			if self.noteNumber <= self.maxNote - 9:
				if 0 in self.soundSet: self.playlist.append(['0', 0, -3, 5000])

		if self.noteNumber >= 2:
			if self.noteNumber <= self.maxNote - 7:
				if 2 in self.soundSet: self.playlist.append(['2', -9, 7, 3400])

		# 

		if self.noteNumber <= self.maxNote - 4:
			if 1 in self.soundSet: self.playlist.append(['1', 0, 0, 2700]) # REFERENCE 1

		if self.noteNumber <= self.maxNote - 7:
			if 4 in self.soundSet: self.playlist.append(['4', 0, 0, 2700]) # REFERENCE 4
			if 9 in self.soundSet: self.playlist.append(['9', 0, 0, 3400]) # REFERENCE 9

		if self.noteNumber <= self.maxNote - 8:
			if 1 in self.soundSet: self.playlist.append(['1', 0, 4, 2700])

		if self.noteNumber <= self.maxNote - 12:
			if 0 in self.soundSet: self.playlist.append(['0', 0, 0, 5000]) # REFERENCE 0
			if 3 in self.soundSet: self.playlist.append(['3', 0, 0, 5600]) # REFERENCE 3
			if 11 in self.soundSet: self.playlist.append(['11', 0, 0, 5600]) # REFERENCE 11
			if 12 in self.soundSet: self.playlist.append(['12', 0, 0, 5000]) # REFERENCE 12
			if 13 in self.soundSet: self.playlist.append(['13', 0, 0, 5600]) # REFERENCE 13

		if self.noteNumber <= self.maxNote - 17:
			if 3 in self.soundSet: self.playlist.append(['3', 0, 5, 5600])