#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("is negative")
elif number == 0:
    print("is Zero")
else:
    print("is positive")
