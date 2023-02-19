import functools
import re

neighbours = {}

for line in open("input.txt").readlines():
    source, dest, dist = re.match(r"(.+) to (.+) = (.+)", line).groups()
    if source not in neighbours:
        neighbours[source] = []
    if dest not in neighbours:
        neighbours[dest] = []
    neighbours[source].append((dest, int(dist)))
    neighbours[dest].append((source, int(dist)))

@functools.cache
def traveling(cur, unvisited):
    if len(unvisited) == 0:
        return 0
    return min((d[1] + traveling(d[0], unvisited - frozenset([d[0]])) for d in neighbours[cur] if d[0] in unvisited))

@functools.cache
def traveling2(cur, unvisited):
    if len(unvisited) == 0:
        return 0
    return max((d[1] + traveling2(d[0], unvisited - frozenset([d[0]])) for d in neighbours[cur] if d[0] in unvisited))

u = frozenset(neighbours.keys())
print(min(traveling(start, u-frozenset([start])) for start in neighbours.keys()))
print(max(traveling2(start, u-frozenset([start])) for start in neighbours.keys()))
