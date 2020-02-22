def merge_the_tools(string, k):
    # your code goes here
    ls = len(string)
    us = [string[i:i + k] for i in range(0, ls, k)]
    
    ans = list()
    for u in us:
        val = ""
        s = set(u)
        count = len(u) - len(s)
        if count == 0:
            ans.append(u)
        else:
            for letter in u:
                if s:
                    if letter in s:
                        val += letter
                        s.remove(letter)
            ans.append(val)
    
    print('\n'.join(ans))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    