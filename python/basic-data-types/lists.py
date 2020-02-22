n = int(input())
lst = []
queries = [input().split() for _ in range(n)]

for query in queries:
    request = query[0]
    if request == 'insert':
        lst.insert(int(query[1]), int(query[2]))
    elif request == 'print':
        print(lst)
    elif request == 'remove':
        lst.remove(int(query[1]))
    elif request == 'append':
        lst.append(int(query[1]))
    elif request == 'pop':
        lst.pop()
    elif request == 'reverse':
        lst.reverse()
    elif request == 'sort':
        lst.sort()