def is_repeating(num):
    if(len(set(str(num))) == len(str(num))):
        return True
    return False

print(is_repeating(98))

a = ["abc", "abd", "abdfff", "ab"]

print(sorted(a))



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'rearrangeWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING word as parameter.
#
from itertools import permutations

def rearrangeWord(word):
    perms = [''.join(p) for p in permutations(word)] 
    perms = list(dict.fromkeys(perms))
    perms = sorted(perms)
    if(word == perms[-1]):
        return "no answer"
    for i, w in enumerate(perms):
        if(w == word):
            return perms[i+1]
    


if __name__ == '__main__':
