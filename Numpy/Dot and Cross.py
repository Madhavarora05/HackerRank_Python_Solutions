import numpy

N = int(input())
arr_1 = []
arr_2 = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr_1.append(tmp)
n_arr1 = numpy.array(arr_1)
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr_2.append(tmp)
n_arr2 = numpy.array(arr_2)
print(numpy.dot(n_arr1, n_arr2))