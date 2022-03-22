"""
gonçalo esteves
13.12.2021
"""

from termcolor import colored
import click


@click.command()
@click.argument("number", type=int, default=0)
def start(number):
    if number != 0:
        print(colored(str(number), "cyan") + " : start")
        collatz(number)
    else:
        userinput = input("Insert a number to start the Collatz Conjecture: ")
        if userinput.isdigit():
            print(colored(userinput, "cyan") + " : start")
            collatz(int(userinput))


def collatz(number: int):
    if number == 0:
        print(colored("You can't start with 0.", "red"))
        exit()
    if number % 2 == 0:
        print(colored("/2", "red"))
        number /= 2
    else:
        number = number * 3 + 1
        print(colored("*3+1", "red"))
    if number == 1:
        print(colored("1", "cyan") + " : end")
        return
    else:
        print(colored(str(number), "cyan"))
        collatz(number)


if __name__ == "__main__":
    start()
