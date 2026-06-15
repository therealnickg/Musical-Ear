# Import REQUIRED modules and libraries
import secrets # To use random generator for numbers
from playsound import playsound # To play sounds on computer
from playlist import Playlist # To import playlist array file
from TempWAV import TempWAVfile # To import custom WAV transposer

# Find the maximum note the user can play on their instrument
# Minimum note is obviously assumed to be zero (0)
# Maximum note is always 24 notes higher than the number of frets (2 octaves)
def findMaxPlayableNote(numFrets):
	return 24 + numFrets

# Checks if user input is a valid mode of operation from playlist file
# Must be a number character from 0 to 4 to return True
# Empty string mode may also be accepted (changes to default 1 later)
def isValidMode(mode):
	if mode == "0":
		return True
	if mode == "1" or mode == "":
		return True
	if mode == "2":
		return True
	if mode == "3":
		return True
	if mode == "4":
		return True
	return False

# Checks if user input is a valid string on the guitar
# Must be a number character from 0 to 6 to return True
# Selecting 0 will choose random string later
# Empty user input may also be accepted (changes to default 0 later)
def isValidGuitarString(guitarStr):
	if guitarStr == "0" or guitarStr == "":
		return True
	if guitarStr == "1":
		return True
	if guitarStr == "2":
		return True
	if guitarStr == "3":
		return True
	if guitarStr == "4":
		return True
	if guitarStr == "5":
		return True
	if guitarStr == "6":
		return True
	return False

# Returns the random reference tone for the string chosen by the user
# The program assumes the user is in standard tuning
# Strings 1-5 have their separate tones, the default return is the 6th string
def createReferenceToneNumber(guitarStr, numFrets):
	# DEBUGGING LINE BELOW (COMMENT OUT)
	#return 23
	if guitarStr == "1":
		return secrets.randbelow(numFrets + 1) + 24
	if guitarStr == "2":
		return secrets.randbelow(numFrets + 1) + 19
	if guitarStr == "3":
		return secrets.randbelow(numFrets + 1) + 15
	if guitarStr == "4":
		return secrets.randbelow(numFrets + 1) + 10
	if guitarStr == "5":
		return secrets.randbelow(numFrets + 1) + 5
	return secrets.randbelow(numFrets + 1) # Base case 6th string

# Introduction
print("\n\nHello, this is the Ear to Instrument Trainer!")
print("This is the random sound practice with the ability to select a string.")

userInput = "N" # DEFAULT "N" sets user up to start the exercise
numberOfFrets = 15 # Number of playable frets on your guitar
# Classical Guitar default is 15
# Acoustic Guitar default is 20
# Electric Guitar default is 22
maxNote = findMaxPlayableNote(numberOfFrets) # Find the maximum playable note on the instrument

# User selects the mode of operation
print("\nModes of Operation:")
print("\t0. On-demand sounds (e.g. weak areas or debugging)")
print("\t1. All the sounds (DEFAULT press ENTER)")
print("\t2. Scales (Major, Minor, Pentatonic, Harmonic, Modes, etc.)")
print("\t3. Triads, Chords, and Arpeggios (7ths, 9ths, Diminished, etc.)")
print("\t4. Licks and Melodies")
print("What mode of operation would you like to select?\n")
modeOfOps = input("Enter a number from 0 to 4: ")
while (not isValidMode(modeOfOps)):
	print("That was not a valid number from 0 to 4.")
	modeOfOps = input("Enter a number from 0 to 4: ")
# If the mode is an empty string, it will changed to the default mode 1
if (modeOfOps == ""):
	modeOfOps = "1"

# User picks string and random note on string (reference tone) is selected
print("\n\n\nWhat guitar string would you like to use for this session?")
print("Choose a number from 1 to 6. Choose 0 (or press ENTER) for random string.\n")
referenceStringInput = input("Enter a number from 0 to 6: ")
while (not isValidGuitarString(referenceStringInput)):
	print("That was not a valid number from 0 to 6.")
	referenceStringInput = input("Enter a number from 0 to 6: ")
# If the input is an empty string, it will changed to the default mode 0
if (referenceStringInput == ""):
	referenceStringInput = "0"
# If a random string is selected (0), then automatically choose one for the user
if (referenceStringInput == "0"):
	randoString = secrets.randbelow(6) + 1
	referenceStringInput = str(randoString)
	print("\nRandomly chosen string: " + str(referenceStringInput))

# Generates random reference tone for exercise
referenceTone = createReferenceToneNumber(referenceStringInput, numberOfFrets)

# Generates an empty playlist (using Playlist class)
# Adds sounds based on reference tone 
pList = Playlist(modeOfOps, referenceTone, maxNote)
sound = pList.getNextSound()
TempWAVfile(sound) # Is this one required? I'm not sure since 1st node is dummy
count = 0 # Counter for how many sounds have been played

print("\nN for new sound, R to repeat interval, T to reset reference tone.")
print("Nothing to exit.")

# FLOW LOGIC FOR THE PROGRAM BELOW

while userInput != "":

	# "R" to play the same sounds again
	if userInput.upper() == "R":
		playsound("Sounds/Notes/"+str(referenceTone)+'.wav') # Play original reference tone
		playsound('Sounds/Temp.wav') # Play mystery sound

	# "N" to generate new random sound for user to figure out
	elif userInput.upper() == "N":

		count = count + 1 # Increase count by one

		if len(pList.playlist) > 0:
			sound = pList.getNextSound()
			TempWAVfile(sound) # Generates WAV file of sound
			# Print current count of sounds played and remaining sounds in bank
			print("\nCount: " + str(count) + ", Remaining: " + str(pList.lengthPlaylist()))
			print("Current playing: ID_" + sound[0] + "\n")

			playsound("Sounds/Notes/"+str(referenceTone)+'.wav') # Play original reference tone
			playsound('Sounds/Temp.wav') # Play mystery sound
			
		elif pList.lengthPlaylist() == 0:
			print("Playlist is empty.")

	# "T" to reset the reference tone
	elif userInput.upper() == "T":
		referenceTone = createReferenceToneNumber(referenceStringInput)
		userInput = "N"

	# Else let user know command was invalid
	else:
		print("That is not a recognized command.")
		print("\nN for new sound, R to repeat interval, T to reset reference tone.")
		print("Nothing to exit.")
	
	# Ask the user what they want to do next
	userInput = input("What would you like to do? ")
