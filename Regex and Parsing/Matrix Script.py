import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    matrix = list(zip(*matrix))

t=[]
for i in range(m):
    for j in range(n):
        t.append(matrix[j][i])
    
s = ''.join(t)
    
path = re.compile(r'\b[ !@#$%&]+\b', re.M)
k = re.sub(path, ' ', s)
print(k)