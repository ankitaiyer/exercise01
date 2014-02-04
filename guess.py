import random

print "Hey there, welcome to our guessing game!"
print "What's your name?"
name = raw_input("> ")

computer_number = random.randint(1, 100)

# ask player to choose a random number between 1 and 100
print "%s, I'm thinking of a number between 1 and 100." % name,
print "Try to guess my number."

count = 0

while True:
    count += 1
    user_guess = int(raw_input("> "))

    if user_guess < 1 or user_guess > 100:
        print "Sorry, that doesn't seem to be between 1 and 100.",
        print "Please enter a number between 1 and 100."
    elif user_guess > computer_number:
        print "Your guess is too high, try again."
    elif user_guess < computer_number:
        print "Your guess is too low, try again."
    else:
        print "Congratulations, %s! You found my number, %d, in %d attempts!" % (name, computer_number, count)
        break