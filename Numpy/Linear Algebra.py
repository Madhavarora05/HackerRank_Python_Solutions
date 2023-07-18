import numpy

N=int(input())
arr=[]
for _ in range(N):
    row=list(map(float,input().split()))
    arr.append(row)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(arr))
    