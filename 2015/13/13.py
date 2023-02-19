import re
import itertools

def eval_perm(perm, vals):
    s = 0
    n = len(perm)
    for i, c in enumerate(perm):
        s += vals[c][perm[(i-1)%n]] + vals[c][perm[(i+1)%n]]
    return s

d = {}

for line in open("input.txt").readlines():
    a, t, num, b = re.match(r"(\w+) would (\w+) (\d+).* (\w+)\.", line).groups()
    n = int(num)
    if t == "lose":
        n *= -1
    if a not in d:
        d[a] = {"YOU": 0}
    d[a][b] = n

print(max(eval_perm(p, d) for p in itertools.permutations(d.keys())))
d["YOU"] = {name: 0 for name in d.keys()}
print(max(eval_perm(p, d) for p in itertools.permutations(d.keys())))
