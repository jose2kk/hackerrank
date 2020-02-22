import re
string = input()
pattern = re.compile(input())
r = pattern.search(string)

if not r: 
    print((-1, -1))

while r:
    print(f'({r.start()}, {r.end()-1})')
    r = pattern.search(string,r.start() + 1)