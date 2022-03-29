try:
    from termcolor import colored
    import click
except ModuleNotFoundError:
    print("please install the required modules with: \npy -m pip install -r './collatz_conjecture/requirements.txt'")
    exit(1)


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
        exit(0)
    if number % 2 == 0:
        print(colored("/2", "red"))
        number /= 2
    else:
        number = number * 3 + 1
        print(colored("*3+1", "red"))
    if number == 1:
        print(colored("1", "cyan") + " : end")
        exit(0)
    else:
        print(colored(str(number), "cyan"))
        collatz(number)


if __name__ == "__main__":
    start()
