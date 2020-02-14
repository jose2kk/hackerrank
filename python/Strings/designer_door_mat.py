N, M = input().split()
N = int(N)
M = int(M)

# Top Matrix
for i in range(N // 2):
    print((".|." * (1 + 2 * i)).center(M, '-'))

# Mid Matrix
print("WELCOME".center(M, '-'))

# Bottom Matrix
for j in range(N // 2):
    print((".|." * ((2 * N // 2) - 2 - 2 * j)).center(M, '-'))