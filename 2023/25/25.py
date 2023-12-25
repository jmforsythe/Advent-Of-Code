edges = set()
nodes = set()
for line in open("input.txt"):
    a, b = line.strip().split(": ")
    nodes.add(a)
    for c in b.split(" "):
        edges.add((a,c))
        nodes.add(c)

from random import choice
while True:
    subsets = [{node} for node in nodes]

    while len(subsets) > 2:
        random_edge = choice(list(edges))
        v1, v2 = random_edge
        containing_subset_1 = next(s for s in subsets if v1 in s)
        containing_subset_2 = next(s for s in subsets if v2 in s)
        if containing_subset_1 != containing_subset_2:
            containing_subset_1 |= containing_subset_2
            subsets.remove(containing_subset_2)
    count = 0
    for u1, u2 in edges:
        subset_1 = next(s for s in subsets if u1 in s)
        subset_2 = next(s for s in subsets if u2 in s)
        if subset_1 != subset_2:
            count += 1
    if count < 4:
        break

assert(len(subsets) == 2)
prod = 1
for s in subsets:
    prod *= len(s)
print(prod)

