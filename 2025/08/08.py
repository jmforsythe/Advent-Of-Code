coords = {i: tuple(map(int, line.split(","))) for i, line in enumerate(open("input.txt").read().splitlines())}
distances = [[(coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2 + (coords[i][2]-coords[j][2])**2 for j in coords] for i in coords]
distances_flat = sorted([(distances[i][j], i, j) for i in coords for j in coords if i < j])

belongs_to = {i: i for i in coords}
contains = [{i} for i in coords]

def join(a, b):
    if belongs_to[a] != belongs_to[b]:
        old = belongs_to[b]
        for c in contains[old]:
            belongs_to[c] = belongs_to[a]
            contains[belongs_to[a]].add(c)
        contains[old].clear()

for (d2, a, b) in distances_flat[:1000]:
    join(a, b)

out = 1
for i in sorted([len(c) for c in contains])[-3:]:
    out *= i
print(out)

last = 1000-1
while len(contains[belongs_to[0]]) < len(coords):
    last += 1
    d2, a, b = distances_flat[last]
    join(a, b)

print(coords[distances_flat[last][1]][0] * coords[distances_flat[last][2]][0])
