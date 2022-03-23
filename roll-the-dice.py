# roll-the-dice.py
from random import Random


if __name__ == "__main__":
    while True:
        # ask to roll the dice
        rstr = input(f"do you want to roll the dice ? [y/n] : ").lower()

        # check what answer the user gave
        if rstr in "yes" or rstr == "1" or rstr == "true":
            inp = True
        elif rstr in "no" or rstr == "0" or rstr == "false":
            inp = False
        else:
            print("not a right answer")
            continue

        # executing what user chose
        if inp:
            # possible results between 1 and 6 (regular dice)
            print(f"the dice stopped on {Random.randint(Random(), 1, 6)}")
        else:
            print("okay, stopping the program now.")
            exit(0)
