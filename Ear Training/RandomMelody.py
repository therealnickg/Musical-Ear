# Import required modules
import secrets # To use random generator for numbers
from playsound import playsound # To play sounds on computer
from playlist import Playlist # To import playlist array file
from TempWAV import TempWAVfile # To import custom WAV transposer

# Did the user input a valid string on the guitar?
# Must be a character that is a number from 0 to 6 to be true
def isValidGuitarString(guitarStr):
	if guitarStr == "0":
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
	return secrets.randbelow(numFrets + 1)

# Find the maximum note the user can play on their instrument
# Minimum note is obviously assumed to be zero (0)
# Maximum note is always 24 notes higher than the number of frets (2 octaves)
def findMaxPlayableNote(numFrets):
	return 24 + numFrets

# Introduction
print("\n\nHello, this is the Ear to Instrument Trainer!")
print("This is the random sound practice.")

userInput = "R" # Sets user up to start the exercise
numberOfFrets = 15 # Number of playable frets on your guitar
# Classical Guitar default is 15
# Acoustic Guitar default is 20
# Electric Guitar default is 22
maxNote = findMaxPlayableNote(numberOfFrets) # Find the maximum playable note on the instrument

# User picks string and random note on string (reference tone) is selected
print("\nWhat guitar string would you like to use for this session?")
print("Choose a number from 1 to 6. Enter 0 for a random string.")
referenceStringInput = input("Enter a number from 0 to 6: ")
while (not isValidGuitarString(referenceStringInput)):
	print("That was not a valid number from 0 to 6.")
	referenceStringInput = input("Enter a number from 0 to 6: ")

# Generates random reference tone for exercise
referenceTone = createReferenceToneNumber(referenceStringInput, numberOfFrets)

# Generates an empty playlist and adds sounds based on reference tone 
pList = Playlist(referenceTone, maxNote)
sound = pList.getNextSound()
TempWAVfile(sound)

print("\nN for new sound, R to repeat interval, T to reset reference tone.")
print("Nothing to exit.\n")

while userInput != "":


	# "R" to play the same sounds again
	if userInput.upper() == "R":
		playsound("Sounds/Notes/"+str(referenceTone)+'.wav') # Play original reference tone
		playsound('Sounds/Temp.wav') # Play mystery sound

	# "N" to generate new random sound for user to figure out
	elif userInput.upper() == "N":
		if len(pList.playlist) > 0:
			sound = pList.getNextSound()
			TempWAVfile(sound)
			playsound("Sounds/Notes/"+str(referenceTone)+'.wav') # Play original reference tone
			playsound('Sounds/Temp.wav') # Play mystery sound
		elif len(pList.playlist) == 0:
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
