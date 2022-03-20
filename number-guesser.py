# number guesser
from random import Random

min = 0
max = 255
toGuess = Random.randint(Random(), min, max)
guessed = False
tries = 0


if __name__ == "__main__":
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
