import numpy

n = int(input())
arrs = [
    [
        input().split()
        for _ in range(n)
    ]
    for __ in range(2)
    ]

arr1 = numpy.array(arrs[0], int)
arr2 = numpy.array(arrs[1], int)

print(numpy.dot(arr1,arr2))