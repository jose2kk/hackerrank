n = int(input())
s = set(map(int, input().split()))
N = int(input())
queries = [
    input().split()
    for _ in range(N)
    ]

for query in queries:
    req = query[0]
    if req == 'pop':
        s.pop()
    elif req == 'remove' and int(query[1]) in s:
            s.remove(int(query[1]))
    elif req == 'discard':
        s.discard(int(query[1]))

print(sum(s))