# password-gen
# wip
import string
import random


def getanswer(answer: str):
    if answer.lower() in "yes":
        return True
    elif answer.lower() in "no":
        return False
    else:
        return None


def getsize():
    sizeinput = input("Number of characters? (default: 12) : ")
    if sizeinput.isnumeric():
        size = int(sizeinput)
    else:
        size = 12


def getspecialchar():
    chars = input("Special chars like !@,.-' ? [y/n] (default: yes) : ")
    if chars is None:
        haschars = True
    else:
        haschars = chars


def getnumbers():
    numbers = input("Numbers 0-9 ? [y/n] (default: yes) : ")
    if numbers is None:
        hasnumbers = True
    else:
        hasnumbers = numbers


def getletters():
    letters = input("Letters a-z ? [y/n] (default: yes) : ")
    if letters is None:
        hasletters = True
    else:
        hasletters = letters


def getinputs():
    getsize()
    getletters()


def createpassword():
    for i in range(0, size):
        print(i)


if __name__ == "__main__":
    print("Password generation script.")
    getinputs()
    getnumbers()
    getspecialchar()
    createpassword()
