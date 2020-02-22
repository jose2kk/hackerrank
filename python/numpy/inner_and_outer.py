import numpy

arrs = [
    input().split()
    for _ in range(2)
]

arr1 = numpy.array(arrs[0], int)
arr2 = numpy.array(arrs[1], int)

print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))