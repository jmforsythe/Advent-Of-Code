out = 0
out2 = 0
for line in open("input.txt"):
    nums = [int(i) for i in line.strip().split()]
    diffs = [nums]
    while any(i for i in diffs[-1]):
        diffs.append([diffs[-1][i+1]-diffs[-1][i] for i in range(len(diffs[-1])-1)])
    lefts = [None for d in diffs]
    diffs[-1].append(0)
    lefts[-1] = 0
    for i in range(len(diffs)-1, 0, -1):
        diffs[i-1].append(diffs[i-1][-1] + diffs[i][-1])
        lefts[i-1] = diffs[i-1][0] - lefts[i]
    out += diffs[0][-1]
    out2 += lefts[0]
print(out)
print(out2)
