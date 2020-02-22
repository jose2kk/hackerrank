import numpy

n, m = input().split()
n = int(n)
m = int(m)

arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.product(numpy.sum(arr, axis = 0)))