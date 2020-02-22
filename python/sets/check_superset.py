A = set(input().split())
lA = len(A)

ans = []
for _ in range(int(input())):
    B = set(input().split())
    lB = len(B)
    lAB = len(B.intersection(A))
    ans.append(lA != lB and lAB == lB)
    
print(all(ans))