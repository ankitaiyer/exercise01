import random

print "Hey there, welcome to our guessing game!"
print "What's your name?"
name = raw_input("> ")

computer_number = random.randint(0, 100)

# ask player to choose a random number between 1 and 100
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name

# while True:
#     user_guess = int(raw_input("> "))

