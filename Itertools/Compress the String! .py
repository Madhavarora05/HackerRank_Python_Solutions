from itertools import *
S=input()
for k,c in groupby(S):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
