import numpy

n, m = input().split()
n = int(n)
m = int(m)

arr = [
    input().split()
    for _ in range(n)
    ]

arr = numpy.array(arr, int)

min_ = numpy.min(arr, axis = 1)
print(numpy.max(min_))