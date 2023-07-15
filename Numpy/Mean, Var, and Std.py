import numpy

N, M = map(int, input().split())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
n_arr = numpy.array(arr)
print(numpy.mean(n_arr, axis=1))
print(numpy.var(n_arr, axis=0))
print(round(numpy.std(n_arr, axis=None), 11))