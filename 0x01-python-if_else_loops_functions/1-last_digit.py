#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
if num_str[-1] == '0':
    print(f'Last digit of {num_str} is {num_str[-1]} and is 0')
elif num_str[-1] > '5':
    print(f'Last digit of {num_str} is {num_str[-1]} and is greater than 5')
elif num_str[-1] < '6' and num_str[-1] != '0':
    print(f'Last digit of {num_str} is {num_str[-1]} and
        is less than 6 and not 0')
