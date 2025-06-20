# import required module
import secrets
from playsound import playsound

print("\n\n\nHello, this is the Ear to Instrument Trainer!")
print("This is the random interval practice.")
print("\nN for new sound, ")
print("R to repeat sound,")
print("T to generate new reference tone,")
print("Nothing to exit.")

### Global Variables ###
maxInterval = 12 # Maximum interval that user can figure out
# Number of comfortably playable frets on your guitar
numberOfFrets = 12 # 17 for electric; 12 for classical
maxNotes = 46 # Maximum notes available to play on the instrument

userInput = "n" # Sets user up to start the exercise
intervalNumber = 0 # Default 0 interval before generating random interval

# Is the user input a valid string on the guitar?
# Must be a character that is a number from 1 to 6 to be true
# The number 0 also returns true as this stands for a random string
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
# String 0 returns a random number from anywhere
def createReferenceToneNumber(s):
	if s == "0":
		return secrets.randbelow(maxNotes+1)
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

# Returns a random number bank of intervals depending
def createIntervalBank(s):
	# Create bank and shuffle it keeping in mind what string is chosen
	bank = []
	if (s == "1"):
		bank = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5]
	elif (s == "2"):
		bank = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
	elif (s == "5"):
		bank = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
	elif (s == "6"):
		bank = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
	else:
		bank = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
	for i in bank:
		j = secrets.randbelow(len(bank))
		temp = bank[i]
		bank[i] = bank[j]
		bank[j] = temp
	bank.insert(0,0) # Add dummy number at first index
	return bank

print("\nWhat guitar string would you like to use for this session?")
print("Choose a number from 1 to 6. Enter 0 for a random string.")
referenceStringInput = input("Enter a number from 0 to 6: ")
while (not isValidGuitarString(referenceStringInput)):
	print("That was not a valid number from 0 to 6.")
	referenceStringInput = input("Enter a number from 0 to 6: ")

# Generates random reference tone for exercise
referenceTone = createReferenceToneNumber(referenceStringInput)
intervalBank = createIntervalBank(referenceStringInput)

while userInput != "":

	# Generate new random interval number for user to figure out
	if userInput == "n" or userInput == "N":

		# Do not let the program crash due to an empty array
		condition = False # Condition to be satisfied in while loop
		while not condition and len(intervalBank) > 1:
			intervalBank.pop(0) # Remove first number
			intervalNumber = intervalBank[0] # Take the next interval from the bank

			# The sum of the referenceTone + intervalNumber must be between 0 and maxNotes
			if referenceTone + intervalNumber >= 0 and referenceTone + intervalNumber <= maxNotes:
				condition = True

		if condition:
			playsound("Sounds/Notes/"+str(referenceTone)+'.WAV') # Play original reference tone
			playsound("Sounds/Notes/"+str(referenceTone + intervalNumber)+'.WAV') # Play mystery interval
		else:
			print("Interval bank is empty.")

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
		print("\nN for new sound, ")
		print("R to repeat sound,")
		print("T to generate new reference tone,")
		print("Nothing to exit.")
	

	userInput = input("What would you like to do? ")