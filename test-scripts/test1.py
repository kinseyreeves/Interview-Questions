#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'rotateTheString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING originalString
#  2. INTEGER_ARRAY direction
#  3. INTEGER_ARRAY amount
#

def rotateTheString(originalString, direction, amount):
    
    for i in range(0, len(direction)):
        amount_ = amount[i] % len(originalString)
        originalString = rotate(originalString, direction[i], amount_)
    
    return originalString

def rotate(string, direction, amount):
    while amount > 0:
        if(direction == 1):
            string = string[-1] + string[0:-1]
        else:
            string = string[1:] + string[0]
        amount -=1
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    originalString = input()

    direction_count = int(input().strip())

    direction = []

    for _ in range(direction_count):
        direction_item = int(input().strip())
        direction.append(direction_item)

    amount_count = int(input().strip())

    amount = []

    for _ in range(amount_count):
        amount_item = int(input().strip())
        amount.append(amount_item)

    result = rotateTheString(originalString, direction, amount)

    fptr.write(result + '\n')

    fptr.close()


print(rotate("hello", 1, 1))
print(rotate("hello", 1, 1))

print(rotate2)