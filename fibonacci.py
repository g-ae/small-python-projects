"""
fibonacci sequence
checks if the entered number is part of the fibonacci sequence
"""
fibonacci = [0, 1]


def findout(number: int):
    i = 2
    while number not in fibonacci:
        nextnb = fibonacci[i - 2] + fibonacci[i - 1]
        print(nextnb)
        fibonacci.append(nextnb)
        if nextnb > number:
            return False
        i += 1
    return True


def play():
    userin = input("Number to check in the fibonnaci sequence : ")
    if userin.isnumeric():
        print(findout(int(userin)))
    else:
        print("not a number.")
        play()


if __name__ == "__main__":
    play()
