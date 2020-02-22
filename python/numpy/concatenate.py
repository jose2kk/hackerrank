import numpy as np

n, m, p = list(map(int, input().split()))
n_arrays = np.array([input().split() for _ in range(n)], int)
m_arrays = np.array([input().split() for _ in range(m)], int)

print(np.concatenate((n_arrays, m_arrays), axis=0).reshape(m+n,p))