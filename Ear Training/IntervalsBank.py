# import required module
import secrets
from playsound import playsound

print("\n\n\nHello, this is the Ear to Instrument Trainer!")
print("This is the random interval practice.")
print("\nN for new sound, R to repeat interval,\nNothing to exit.")

userInput = "n" # Sets user up to start the exercise
maxInterval = 12 # Maximum interval that user can figure out
maxNotes = 46 # Maximum notes available to play on the instrument

referenceTone = secrets.randbelow(maxNotes+1) # Generates random reference tone for exercise
intervalNumber = 0 # Default 0 interval before generating random interval

# Create bank and shuffle it
intervalBank = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
for i in intervalBank:
	j = secrets.randbelow(len(intervalBank))
	temp = intervalBank[i]
	intervalBank[i] = intervalBank[j]
	intervalBank[j] = temp
intervalBank.insert(0,0) # Add dummy number at first index

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

	# Let user know command was invalid
	else:
		print("That is not a recognized command.")
		print("\nN for new sound, R to repeat interval,\nNothing to exit.")
	

	userInput = input("What would you like to do? ")