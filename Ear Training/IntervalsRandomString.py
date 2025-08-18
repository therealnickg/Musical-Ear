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
print("This is the random interval practice with the ability to choose which string.")
print("\nN for new sound, R to repeat interval,\nNothing to exit.")

userInput = "n" # Sets user up to start the exercise
maxInterval = 12 # Maximum interval that user can figure out
maxNotes = 46 # Maximum notes available to play on the instrument
intervalNumber = 0 # Default 0 interval before generating random interval

print("\nWhat guitar string would you like to use for this session?")
print("Choose a number from 1 to 6. Enter 0 for a random string.\n")
referenceStringInput = input("Enter a number from 0 to 6: ") # Data type is String not Integer
# Make sure the user is typying in a valid string number (0 for random, or 1 - 6)
while (not isValidGuitarString(referenceStringInput)):
	print("That was not a valid number from 0 to 6.")
	referenceStringInput = input("Enter a number from 0 to 6: ")
# If a random string is selected (0), then automatically choose one for the user
if (referenceStringInput == "0"):
	randoString = secrets.randbelow(6) + 1
	print("Randomly chosen string: " + str(randoString))
	referenceStringInput = str(randoString)
print() # Empty print statement for better spacing

# Generates random reference tone for exercise
referenceTone = createReferenceToneNumber(referenceStringInput)
count = 0 # Counter for how many sounds have been played

while userInput != "":

	# Generate new random interval number for user to figure out
	if userInput == "n" or userInput == "N":

		count = count + 1 # Increase count by one
		
		# Interval may go up or down, randomly
		intervalNumber = secrets.randbelow(maxInterval+1) # Generate random interval
		if secrets.randbelow(2) == 1:
			intervalNumber = intervalNumber * -1

		# The sum of the referenceTone + intervalNumber must NOT be negative
		while referenceTone + intervalNumber < 0 or referenceTone + intervalNumber > maxNotes:
			intervalNumber = secrets.randbelow(maxInterval+1) # Generate random interval
			if secrets.randbelow(2) == 1: # Interval may go up or down randomly
				intervalNumber = intervalNumber * -1
		
		print("Count: " + str(count))
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
