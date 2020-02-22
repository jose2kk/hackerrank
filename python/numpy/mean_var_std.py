import numpy

numpy.set_printoptions(legacy='1.13')

n, m = input().split()
n = int(n)
m = int(m)

arr = [
    input().split()
    for _ in range(n)
    ]

arr = numpy.array(arr, int)

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))