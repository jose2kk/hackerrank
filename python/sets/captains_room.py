k = int(input())
rooms = list(map(int, input().split()))

total = sum(rooms)
distinct_rooms = set(rooms)
captain = (k * sum(distinct_rooms) - total) // (k-1)

print(captain)