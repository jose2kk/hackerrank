import numpy as np

n, m = list(map(int, input().split()))
arr1 = np.array([input().split() for _ in range(n)], int)
arr2 = np.array([input().split() for _ in range(n)], int)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
print(arr1 ** arr2)