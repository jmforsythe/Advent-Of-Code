patterns = set(open("input.txt").readline().strip().split(", "))
max_len = max(len(p) for p in patterns)

import functools
@functools.cache
def ways(s):
    return bool(s in patterns) + sum(ways(s[i:]) for i in range(min(max_len, len(s))+1) if s[:i] in patterns)

print(sum([ways(l)>0 for l in open("input.txt").read().splitlines()[2:]]))
print(sum([ways(l) for l in open("input.txt").read().splitlines()[2:]]))
