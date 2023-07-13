import numpy

def arrays(arr):
    N = numpy.array(arr,float)   
    return(N[::-1])

arr = input().strip().split(' ')
result = arrays(arr)
print(result)