def wrapper(f):
    def fun(l):
        # complete the function
        l = [
            '+91 ' + number[-10:-5] + ' ' + number[-5:]
            for number in l    
        ]
        print(*sorted(l), sep='\n')
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 