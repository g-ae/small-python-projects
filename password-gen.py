# password-gen
import string
from random import Random
import os

# clear
os.system('cls' if os.name=='nt' else 'clear')

# possibilities for password
letters = string.ascii_letters
chars = string.punctuation
numbers = string.hexdigits.split('a')[0]


def getanswer(answer: str):
    if answer.lower() in "yes":
        return True
    elif answer.lower() in "no":
        return False
    else:
        return None


def getsize() -> int:
    sizeinput = input("Number of characters? (default: 12) (max: 10000) : ")
    if sizeinput == "":
        return 12
    if sizeinput.isnumeric():
        if int(sizeinput) > 10000:
            print(f"{sizeinput} is too big ! Max size is 10000.")
            return getsize()
        return int(sizeinput)
    else:
        print(f"{sizeinput} is not a number !")
        return getsize()


def getspecialchar() -> bool:
    chars = input("Special chars like !@,.-' ? [y/n] (default: yes) : ")
    if chars == "":
        return True
    else:
        haschars = getanswer(chars)
        if haschars is None:
            print(f"{chars} is not a possible answer.")
            return getspecialchar()
        else:
            return haschars


def getnumbers() -> bool:
    numbers = input("Numbers 0-9 ? [y/n] (default: yes) : ")
    if numbers == "":
        return True
    else:
        hasnumbers = getanswer(numbers)
        if hasnumbers is None:
            print(f"{numbers} is not a possible answer.")
            return getnumbers()
        else:
            return hasnumbers


def getletters() -> bool:
    letters = input("Letters a-z ? [y/n] (default: yes) : ")
    if letters == "":
        return True
    else:
        hasletters = getanswer(letters)
        if hasletters is None:
            print(f"{letters} is not a possible answer.")
            return getnumbers()
        else:
            return hasletters


def createpassword(size, hasletters, hasnumbers, hasspecialchars) -> str:
    possibility = []
    password = ""
    if hasletters:
        for l in letters:
            possibility.append(l)
    if hasnumbers:
        for nb in numbers:
            possibility.append(nb)
    if hasspecialchars:
        for c in chars:
            possibility.append(c)

    for i in range(0, size):
        password += Random.choice(Random(), possibility)

    print(f"Done !\nYour password is {password}")


if __name__ == "__main__":
    print("Password generation script.")
    pwsize = getsize()
    pwhasletters = getletters()
    pwhasnumbers = getnumbers()
    pwhasspecialchars = getspecialchar()
    pw = createpassword(pwsize, pwhasletters, pwhasnumbers, pwhasspecialchars)
