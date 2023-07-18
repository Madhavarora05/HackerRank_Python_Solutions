import numpy

nums = tuple(map(int, input().split()))
print(numpy.zeros(nums, dtype = numpy.int))
print(numpy.ones(nums, dtype = numpy.int))


# In my case there was error for this that
# there is no attribute int of numpy 
#then just change int --> int64