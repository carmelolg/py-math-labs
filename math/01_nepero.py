#!/usr/bin/env python3

import argparse
import random

parser = argparse.ArgumentParser(description='Nepero number calculation')
parser.add_argument("-n", default=500000, type=int, help="Distribution magnitude")

args = parser.parse_args()
magnitude = args.n

distribution = []

# For x times, sum random numbers between 0 and 1 till the sum is equal or greater than 1.
# Let count the number of integers used for this sum. Put the count in a list (called distribution).
# The average of this distribution is the Nepero number

for i in range(magnitude):
    count = 0
    j = 0
    while j <= 1:
        j += random.uniform(0, 1)
        count = count + 1
    distribution.append(count)

nepero = sum(distribution) / len(distribution)

print(nepero)
