import numpy

arr = numpy.array(input().split(), float)
x = int(input())

print(numpy.polyval(arr, x))