n, m = input().split()
n = int(n)
m = int(m)

arr = sorted(list(map(int, input().split())))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

arr_ = set(arr)
arrA = sorted(list(arr_.intersection(A)))
arrB = sorted(list(arr_.intersection(B)))

happiness = 0

while arr:
    val = arr[0]
    del arr[0]
    if arrA:
        if val == arrA[0]:
            happiness += 1
            if arr:
                if val != arr[0]:
                    del arrA[0]
    if arrB:
        if val == arrB[0]:
            happiness -= 1
            if arr:
                if val != arr[0]:
                    del arrB[0]
    if not arrA and not arrB:
        break

print(happiness)