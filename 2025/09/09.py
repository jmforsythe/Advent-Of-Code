points = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in open("input.txt").read().splitlines()]
print(max((abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1) for a in points for b in points))

from collections import defaultdict

edges_on_i = defaultdict(list)
edges_on_j = defaultdict(list)

for a, b in zip(points, points[1:]+[points[0]]):
    if a[0] == b[0]:
        edges_on_i[a[0]].append((min(a[1],b[1]), max(a[1],b[1])+1))
    elif a[1] == b[1]:
        edges_on_j[a[1]].append((min(a[0],b[0]), max(a[0],b[0])+1))

for i in edges_on_i:
    edges_on_i[i].sort()
for j in edges_on_j:
    edges_on_j[j].sort()

def ranges_intersect(left1, right1, left2, right2):
    return max(left1,left2) < min(right1,right2)

out = 0

for a in points:
    for b in points:
        valid = True
        up = min(a[0],b[0])
        down = max(a[0],b[0])
        left = min(a[1],b[1])
        right = max(a[1],b[1])
        for i in edges_on_i:
            if i not in range(up+1, down-1):
                continue
            for edge in edges_on_i[i]:
                if ranges_intersect(left, right, edge[0]+1, edge[1]-1):
                    valid = False
                    break
        if not valid:
            continue
        for j in edges_on_j:
            if j not in range(left+1, right-1):
                continue
        for j in range(left+1, right-1):
            for edge in edges_on_j[j]:
                if ranges_intersect(up, down, edge[0]+1, edge[1]-1):
                    valid = False
                    break
        if valid:
            out = max(out, (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1))

print(out)
