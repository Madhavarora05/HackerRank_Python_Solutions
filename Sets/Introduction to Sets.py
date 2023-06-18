def average(array):
    sum1=0
    for i in set(array):
        sum1+=i
    avg=sum1/len(set(array))
    return "{:.3f}".format(avg)