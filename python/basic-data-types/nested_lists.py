d = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if str(score) in d.keys():
        d[str(score)].append(name)
    else:
        d[str(score)] = [name]

scores = sorted(map(float, d.keys()))

for i in range(len(scores)):
    if scores[i] != scores[i+1]:
        for name in sorted(d[str(scores[i+1])]):
            print(name)
        break