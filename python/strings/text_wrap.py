import textwrap

def wrap(string, max_width):
    ans = []
    for i in range(len(string) // max_width):
        ans.append(string[i * max_width: (i+1) * max_width])
    if not len(string) % max_width == 0:
        ans.append(string[len(string)-len(string)%max_width:])
    return '\n'.join(ans)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)