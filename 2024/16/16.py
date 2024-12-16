grid = {i+1j*j: c for i,line in enumerate(open("input.txt").read().splitlines()) for j,c in enumerate(line)}
from heapq import heappush, heappop
costs = {}
prev = {}
heap = [(0, 0, c, 1j, c, 1j) for c in grid if grid[c] == "S"]
entry_order = 0
while heap:
    cost, _, pos, d, prev_pos, prev_d = heappop(heap)
    if (pos, d) in costs and costs[(pos, d)] < cost:
        continue
    entry_order += 1
    costs[(pos, d)] = cost
    if (pos, d) not in prev:
        prev[(pos, d)] = set()
    prev[(pos, d)].add((prev_pos, prev_d))
    heappush(heap, (cost+1000, entry_order, pos, d*1j, pos, d))
    entry_order += 1
    heappush(heap, (cost+1000, entry_order, pos, d*-1j, pos, d))
    if grid[pos+d] != "#":
        entry_order += 1
        heappush(heap, (cost+1, entry_order, pos+d, d, pos, d))

print(min(costs[(c,d)] for c,d in costs if grid[c] == "E"))
stack = [(c,d) for c,d in costs if grid[c] == "E"]
seen = set()
while stack:
    top = stack.pop()
    for n in prev[top]:
        if n not in seen:
            stack.append(n)
        seen.add(n)
print(len({pos for pos,dir in seen}))
