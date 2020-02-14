n = int(input())
set_1 = set(map(int, input().split()))

for _ in range(int(input())):
    query = input().split()[0]
    set_2 = set(map(int, input().split()))
    if query == 'intersection_update':
        set_1.intersection_update(set_2)
    elif query == 'update':
        set_1.update(set_2)
    elif query == 'symmetric_difference_update':
        set_1.symmetric_difference_update(set_2)
    elif query == 'difference_update':
        set_1.difference_update(set_2)
        
print(sum(set_1))