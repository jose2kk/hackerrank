import numpy

n = int(input())

arr = [
    input().split()
    for _ in range(n)
    ]

arr = numpy.array(arr, float)

print(round(numpy.linalg.det(arr),2))