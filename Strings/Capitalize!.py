#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ans =""
    l = s.split(" ")
    for i in l:
        if i.isdigit():
            ans += i +" "
        else:
            ans+= i.capitalize()+" "
    return ans.strip()
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
