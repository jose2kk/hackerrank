t = int(input())

ans = []
for _ in range(t):
    n1 = int(input())
    A = set(input().split())
    n2 = input()
    B = set(input().split())
    ans.append(len(A.intersection(B)) == n1)
    
print('\n'.join(map(str, ans)))