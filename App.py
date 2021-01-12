#!/usr/bin/
import random

# User set Lower number
L = int(input("Enter Lower bound: > "))
# User set Upper number
H = int(input("Enter Upper bound: > "))


count = 1

# Generate random number
the_number = random.randrange(L, H)
# in put for First guess
guess = int(input("Guess a number: > "))

# While loop
while the_number != guess:

    if guess > the_number:
        print("Too High!")

    if guess < the_number:
        print("Too Low!")

    # Count Attempts
    count += 1

    print("attempt ", count)
    guess = int(input("Guess new Number: > "))

print("Congratulations you did it in", count, "Try")
