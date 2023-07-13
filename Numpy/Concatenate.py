import numpy

N , M , P = map(int,input().split())
arr1=[]
arr2=[]
for _ in range(N):
    row=list(map(int,input().split()))
    arr1.append(row)
for _ in range(M):
    row=list(map(int,input().split()))
    arr2.append(row)
n_arr1 = numpy.array(arr1)
n_arr2 = numpy.array(arr2)
print(numpy.concatenate((n_arr1, n_arr2), axis=0))