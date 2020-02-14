import re
pattern = re.compile(r'(?<=[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])' + \
    '[AEIOUaeiou]{2,}(?=[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])')

flag = True
for match in re.findall(pattern, input()):
    print(match)
    flag = False

if flag:
    print(-1)