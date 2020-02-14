def average(array):
    # your code goes here
    distinct_array = set(array)
    return sum(distinct_array) / len(distinct_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)