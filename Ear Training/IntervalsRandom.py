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

while userInput != "":

	# Generate new random interval number for user to figure out
	if userInput == "n" or userInput == "N":

		intervalNumber = secrets.randbelow(maxInterval+1) # Generate random interval
		if secrets.randbelow(2) == 1: # Interval may go up or down randomly
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

	# Let user know command was invalid
	else:
		print("That is not a recognized command.")
		print("\nN for new sound, R to repeat interval,\nNothing to exit.")
	

	userInput = input("What would you like to do? ")
