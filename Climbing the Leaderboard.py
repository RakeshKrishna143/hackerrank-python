#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(a,b):
    a = sorted(list(set(a)),reverse = True)
    b.sort(reverse = True)
    j = 0
    l = len(a)
    result = []
    for i in range(len(b)):
        while j<l and b[i]<a[j]:
            j+=1
        result.append(j+1)
    return result[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
