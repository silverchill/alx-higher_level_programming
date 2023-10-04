#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print(f"{number} is 0")
else:
    print("{0} is negative".format(number))
