#!/usr/bin/env python2

# Import Random Module
import random

count = int(input("How many random numbers you want?"))

for r in range(count):
        print(random.randint(0, 10))
