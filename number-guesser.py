"""
number guesser
the script creates a random number and the user has to guess it based on "too high" or "too low" answers
min and max values can be changed through the "min" and "max" variables in the code
"""
from random import Random


if __name__ == "__main__":
    min = 0
    max = 1000
    toGuess = Random.randint(Random(), min, max)
    guessed = False
    tries = 0
    while not guessed:
        tries += 1
        guess = input("guess the number : ")

        if guess.isnumeric():
            guess = int(guess)
        else:
            print("not a number !!!")
            continue
        if guess is toGuess:
            if tries == 1:
                triesstr = "try"
            else:
                triesstr = "tries"
            print(f"nice one you won in {str(tries)} {triesstr}")
            exit(0)
        else:
            if guess > toGuess:
                print("too high !")
            else:
                print("too low !")
