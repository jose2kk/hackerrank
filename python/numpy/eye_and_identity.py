import numpy as np
np.set_printoptions(legacy='1.13')

n, m = tuple(map(int, input().split()))
print(np.eye(n, m))