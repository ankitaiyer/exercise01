# need random module to generate random integer
import random

# greet user and ask for name
print "Hey there, welcome to our guessing game!"
print "What's your name?"
name = raw_input("> ")

# generate random integer between 1 and 100
computer_number = random.randint(1, 100)

# ask player to choose a random number between 1 and 100
print "%s, I'm thinking of a whole number between 1 and 100." % name,
print "Try to guess my number."

# initialize attempt counter
count = 0

# main loop: user guesses
while True:
    # increment the attempt counter
    count += 1

    # get user guess
    user_input = raw_input("> ")

    # check to see if user guess is a number; if not, ask to guess again
    if user_input.isdigit() == False:
        print "Sorry, that doesn't seem to be a whole number."
        print "Please enter a number between 1 and 100."

    else:
        
        # convert user guess to an integer
        user_guess = int(user_input)

        # hints if user guess is incorrect and asks for new guess
        if user_guess < 1 or user_guess > 100:
            print "Sorry, that doesn't seem to be between 1 and 100.",
            print "Please enter a number between 1 and 100."
        elif user_guess > computer_number:
            print "Your guess is too high, try again."
        elif user_guess < computer_number:
            print "Your guess is too low, try again."

        # for correct guess, congratulate and end game
        else:
            print "Congratulations, %s! You found my number, %d, in %d attempts!" % (name, computer_number, count)
            break