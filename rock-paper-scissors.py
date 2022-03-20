# rock paper scissors
from random import Random
import time
possibilities = ["rock", "paper", "scissors"]


def who_won(input1, input2):
    if input1 == "rock":
        if input2 == "paper":
            return input2
        elif input2 == "rock":
            return None
        elif input2 == "scissors":
            return input1
    elif input1 == "paper":
        if input2 == "paper":
            return None
        elif input2 == "rock":
            return input1
        elif input2 == "scissors":
            return input2
    elif input1 == "scissors":
        if input2 == "paper":
            return input1
        elif input2 == "rock":
            return input2
        elif input2 == "scissors":
            return None
    return None


if __name__ == "__main__":
    while True:
        # get inputs
        botinput = Random.choice(Random(), possibilities)
        play = input("What will you play ? [r/p/s] : ")
        if "rock".__contains__(play):
            # played rock
            userinput = "rock"
        elif "paper".__contains__(play):
            # played paper
            userinput = "paper"
        elif "scissors".__contains__(play):
            # player scissors
            userinput = "scissors"
        else:
            print("not a possibility !")
            continue

        # who won
        winner = who_won(botinput, userinput)

        # countdown
        for i in reversed(range(3)):
            print(f"{str(i + 1)}{(i+1)*'.'}")
            time.sleep(0.5)
        print(f"You played {userinput}")
        print(f"Opponent played {botinput}")

        # affichage
        if winner is None:
            # no one won
            print(f"Both players played {winner}")
        elif winner == botinput:
            print("You lost ! Good luck next time.")
        elif winner == userinput:
            print("You won ! Nice one :)")
