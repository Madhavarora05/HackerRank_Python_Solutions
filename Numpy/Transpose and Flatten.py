import numpy
x,y= map(int,input().split())
arr=[]
for _ in range(x):
    row = list(map(int, input().split()))
    arr.append(row)
arr2=numpy.array(arr)
print(numpy.transpose(arr2))
print(arr2.flatten())
