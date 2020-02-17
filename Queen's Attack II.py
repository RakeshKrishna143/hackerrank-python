#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obs):
    l = defaultdict(int)

    l[(r_q-1,c_q-1)]=-1
    if k!=0:
        for i,j in obs:
            l[(i-1,j-1)]=-1

    count = 0
    #up
    j = c_q-1
    for i in range(r_q,n):
        if (i,j) not in l:
            count+=1
        else:
            break 
    print(count)    
    #up right
    j = c_q
    for i in range(r_q,n):
        if j==n:
            break
        elif (i,j) not in l:
            count+=1
            j+=1
        else:
            break 
    print(count)
    #right
    i = r_q-1
    for j in range(c_q,n):
        if (i,j) not in l:
            count+=1
        else:
            break 
    print(count)
    #down right
    j = c_q
    for i in range(r_q-2,-1,-1):
        if j==n:
            break
        elif (i,j) not in l:
            count+=1
            j+=1
        else:
            break
    print(count)

    #down
    j = c_q-1
    for i in range(r_q-2,-1,-1):
        if (i,j) not in l:
            count+=1
        else:
            break
    print(count)
    #down left
    j = c_q-2
    for i in range(r_q-2,-1,-1):
        if j==-1:
            break
        elif (i,j) not in l:
            count+=1
            j-=1
        else:
            break
    print(count)

    #left
    i = r_q-1
    for j in range(c_q-2,-1,-1):
        if (i,j) not in l:
            count+=1
        else:
            break 
    print(count)

    #up left
    j = c_q-2
    for i in range(r_q,n):
        if j==-1:
            break 
        elif (i,j) not in l:
            count+=1
            j-=1
        else:
            break
    print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
