# import required module
import secrets
from playsound import playsound

# Is the user input a valid string on the guitar?
# Must be a character that is a number from 1 to 6 to be true
def isValidGuitarString(s):
	if s == "0":
		return True
	if s == "1":
		return True
	if s == "2":
		return True
	if s == "3":
		return True
	if s == "4":
		return True
	if s == "5":
		return True
	if s == "6":
		return True
	return False

# Returns the random reference tone for the string chosen by the user
# Strings 1-5 have their separate tones, the default return is the 6th st
def createReferenceToneNumber(s):
	numberOfFrets = 17 # Number of comfortably playable frets on your guitar
	if s == "1":
		return secrets.randbelow(numberOfFrets + 1) + 24
	if s == "2":
		return secrets.randbelow(numberOfFrets + 1) + 19
	if s == "3":
		return secrets.randbelow(numberOfFrets + 1) + 15
	if s == "4":
		return secrets.randbelow(numberOfFrets + 1) + 10
	if s == "5":
		return secrets.randbelow(numberOfFrets + 1) + 5
	return secrets.randbelow(numberOfFrets + 1)
	

print("\n\n\nHello, this is the Ear to Instrument Trainer!")
print("This is the random interval practice.")
print("\nN for new sound, R to repeat interval,\nNothing to exit.")

userInput = "n" # Sets user up to start the exercise
maxInterval = 12 # Maximum interval that user can figure out
maxNotes = 46 # Maximum notes available to play on the instrument
intervalNumber = 0 # Default 0 interval before generating random interval

print("\nWhat guitar string would you like to use for this session?")
print("Choose a number from 1 to 6. Enter 0 for a random string.")
referenceStringInput = input("Enter a number from 0 to 6: ")
while (not isValidGuitarString(referenceStringInput)):
	print("That was not a valid number from 0 to 6.")
	referenceStringInput = input("Enter a number from 0 to 6: ")

# Generates random reference tone for exercise
referenceTone = createReferenceToneNumber(referenceStringInput)

while userInput != "":

	# Generate new random interval number for user to figure out
	if userInput == "n" or userInput == "N":

		# Interval may go up or down, randomly
		intervalNumber = secrets.randbelow(maxInterval+1) # Generate random interval
		if secrets.randbelow(2) == 1:
			intervalNumber = intervalNumber * -1

		# The sum of the referenceTone + intervalNumber must NOT be negative
		while referenceTone + intervalNumber < 0 or referenceTone + intervalNumber > maxNotes:
			intervalNumber = secrets.randbelow(maxInterval+1) # Generate random interval
			if secrets.randbelow(2) == 1: # Interval may go up or down randomly
				intervalNumber = intervalNumber * -1
				
		playsound("Sounds/Notes/"+str(referenceTone)+'.WAV') # Play original reference tone
		playsound("Sounds/Notes/"+str(referenceTone + intervalNumber)+'.WAV') # Play mystery interval

	# User chooses to repeat the same interval
	elif userInput == "r" or userInput == "R":
		playsound("Sounds/Notes/"+str(referenceTone)+'.WAV') # Play original reference tone
		playsound("Sounds/Notes/"+str(referenceTone + intervalNumber)+'.WAV') # Play same interval again

	# User chooses to reset the reference tone
	elif userInput == "t":
		referenceTone = createReferenceToneNumber(referenceStringInput)
		userInput = "n"

	# Let user know command was invalid
	else:
		print("That is not a recognized command.")
		print("\nN for new sound, R to repeat interval,\nNothing to exit.")
	

	userInput = input("What would you like to do? ")
