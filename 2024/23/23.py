from collections import defaultdict
nbrs = defaultdict(set)

for line in open("input.txt").read().splitlines():
    a, b = line.split("-")
    nbrs[a].add(b)
    nbrs[b].add(a)

out = set()
for a in nbrs:
    for b in nbrs[a]:
        for c in nbrs[b]:
            if c in nbrs[a]:
                out.add(tuple(sorted((a,b,c))))

print(len([(a,b,c) for a,b,c in out if a[0]=="t" or b[0]=="t" or c[0]=="t"]))

import functools
@functools.cache
def largest_containing_path(path):
    largest = path
    for b in set.intersection(*(nbrs[a] for a in path)):
        if b in path:
            continue
        possible = largest_containing_path(path | frozenset([b]))
        if len(possible) > len(largest):
            largest = possible
    return largest

longest = frozenset()
for n in list(nbrs.keys()):
    possible = largest_containing_path(frozenset([n]))
    if len(possible) > len(longest):
        longest = possible
print(",".join(sorted(list(longest))))
