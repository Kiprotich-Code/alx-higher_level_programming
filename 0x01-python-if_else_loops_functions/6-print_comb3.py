#!/usr/bin/python3

for FirstDigit in range(0, 10):
    for SecondDigit in range(FirstDigit + 1, 10):
        if FirstDigit == 8 and SecondDigit == 9:
            print("{}{}".format(FirstDigit, SecondDigit))
        else:
            print("{}".format(FirstDigit, SecondDigit), end="")
