#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    a = []
    l=len(scores)
    max_count=0
    min_count=0
    max_num = scores[0]
    min_num = scores[0]
    for i in range(1,l):
        if max_num<scores[i]:
            max_num=scores[i]
            max_count+=1
        elif min_num>scores[i]:
            min_num=scores[i]
            min_count+=1
    a.append(max_count)
    a.append(min_count)
    return a
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
