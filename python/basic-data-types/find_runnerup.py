def runner_up(arr):
    for i in range(1,len(arr)):
        if arr[-i-1] < arr[-i]:
            return arr[-i-1]    

if __name__=='__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))

    print(runner_up(arr))