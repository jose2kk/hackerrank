def print_rangoli(n):
    # your code goes here
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    s1 = alphabet[:n]
    s2 = sorted(s1, reverse = True)

    a = []
    for i in range((2 * n - 1)//2):
        s = s2[:i + 1] + sorted(s2[:i])
        ss = "-".join(s)
        a.append(ss.center(4 * n - 3, '-'))
    a.append("-".join(s2[:] + s1[1:]))

    for val in a:
        print(val)
    for val in sorted(a[:-1], reverse = True):
        print(val)