#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    
    print("alice" + str(alice))
    print("scores" + str(scores))
    
    pos = 0

    set_scores = set(scores)
    leng = len(set_scores)
    scores = scores[::-1]
    passed = set()
    output = []
    a_i = 0
    s_i = 0
    
    print("here")
    for a_i, a_score in enumerate(alice):

        while a_score > scores[s_i]:
            passed.add(scores[s_i])
            s_i +=1
            if(s_i==len(scores)-1):
                break
 
        if(a_score == scores[s_i]):
            output.append(leng - len(passed))
        else:
            if(a_score > scores[s_i]):
                output.append(1)
            else:
                output.append(leng - len(passed)+1)

        if(s_i==len(scores)-1):
            break
    
    a_i+=1
    while(a_i < len(alice)):
        if(alice[a_i] >= scores[-1]):
            output.append(1)
        else:
            output.append(leng - len(passed)+1)
        a_i+=1
    print(output)
    return output

                    

        



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
