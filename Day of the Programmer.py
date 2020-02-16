#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(y):
    if y == 1918:
        return '26.09.'+str(y)
    elif ((y<=1917) and (y%4==0) ) or ((y>=1919) and ((y%400==0)or((y%4==0)and(y%100!=0)))):
        return '12.09.'+str(y)
    else:
        return '13.09.'+str(y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
