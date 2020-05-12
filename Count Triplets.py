#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(a, ratio):
    r = Counter(a[1:]) #right side
    l = defaultdict(int) #left side
    c = 0
    for i in range(len(a)):
        if i!=0:
            l[a[i-1]]+=1
            r[a[i]]-=1
        c += l[a[i]/ratio]*r[a[i]*ratio]
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

'''
from collections import defaultdict

a = [1,3,9,9,27,81]
r=3

d1 = defaultdict(int)
d2 = defaultdict(int)
count = 0

for i in reversed(a):
    if i*r in d2:
        count+= d2[i*r]
        
    if i*r in d1:
        d2[i]+=d1[i*r]
        
    d1[i]+=1
    print(d1,d2,count)
    
    
print(count)
        
'''
