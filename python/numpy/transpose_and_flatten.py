import numpy as np

n, m = input().split()
n = int(n)
m = int(m)

arr = np.array([input().split() for _ in range(n)], int)

print(np.transpose(arr))
print(arr.flatten())