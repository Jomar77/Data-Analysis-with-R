#random number generator that relies on normal distribution
# limit the numbers genereated to 1-40
# 6 numbers per entry
# last number must only be from 1-10

import random
import math

def main():
    print("Welcome to the Lottery numbers generator")
    # get the number of entries
    num_entries = int(input("How many entries would you like? "))
    print()
    # get the numbers for each entry
    for i in range(num_entries):
        print("Entry", i+1, end=": ")
        for j in range(6):
            # generate a random number between 1 and 40
            num = math.ceil(random.gauss(20, 10))
            # if the number is less than 1 or greater than 40, generate a new number
            while num < 1 or num > 40:
                num = math.ceil(random.gauss(20, 10))
            print(num, end=" ")
        # generate the last number between 1 and 10
        num = math.ceil(random.gauss(5, 2))
        # if the number is less than 1 or greater than 10, generate a new number
        while num < 1 or num > 10:
            num = math.ceil(random.gauss(5, 2))
        print("Bonus:", num)
    print()

main()