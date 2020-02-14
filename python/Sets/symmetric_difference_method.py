# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
s1 = set(input().split())
n2 = int(input())
s2 = set(input().split())

print(len(s1.symmetric_difference(s2)))