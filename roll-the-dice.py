# roll-the-dice.py
from random import Random


if __name__ == "__main__":
    while True:
        # ask to roll the dice
        rstr = input(f"do you want to roll the dice ? [y/n] : ").lower()

        # check what answer the user gave
        if rstr == "yes" or rstr == "y" or rstr == "1" or rstr == "ye" or rstr == "true":
            inp = True
        elif rstr == "no" or rstr == "n" or rstr == "0" or rstr == "false":
            inp = False
        else:
            print("not a right answer")
            continue

        # executing what user chose
        if inp:
            rolled = Random.randint(Random(), 1, 6)
            print(f"the dice stopped on {rolled}")
        else:
            print("okay, stopping the program now.")
            exit(0)
