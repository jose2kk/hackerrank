m = int(input())
a = set(input().split())
n = int(input())
b = set(input().split())

print('\n'.join(map(str, sorted(map(int, a.symmetric_difference(b))))))