bricks = [((min(x1,x2),min(y1,y2),min(z1,z2)),(max(x1,x2),max(y1,y2),max(z1,z2))) for x1,y1,z1,x2,y2,z2 in map(lambda line: map(int,line.strip().replace("~",",").split(",")), open("input.txt").readlines())]
bricks.sort(key=lambda brick: brick[0][2])

grid = {(x,y,z): str(i) for i, ((x1,y1,z1), (x2,y2,z2)) in enumerate(bricks) for x in range(x1,x2+1) for y in range(y1,y2+1) for z in range(z1,z2+1)}
for i, (((x1,y1,z1), (x2,y2,z2))) in enumerate(bricks):
    while z1 > 1:
        if any((x,y,z1-1) in grid for x in range(x1,x2+1) for y in range(y1,y2+1)):
            break
        z1 -= 1
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x,y,z1] = str(i)
                grid.pop((x,y,z2))
        z2 -= 1

    bricks[i] = ((x1,y1,z1), (x2,y2,z2))

supported_by = {str(i): set() for i in range(len(bricks))}
supports = {str(i): set() for i in range(len(bricks))}
for i, (((x1,y1,z1), (x2,y2,z2))) in enumerate(bricks):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if (x,y,z2+1) in grid:
                supported_by[grid[(x,y,z2+1)]].add(str(i))
                supports[str(i)].add(grid[(x,y,z2+1)])

out = 0
for i in range(len(bricks)):
    if {str(i)} not in supported_by.values():
        out += 1
print(out)

from copy import deepcopy

def disintegrate(s_b, supports, brick):
    supported_by = deepcopy(s_b)
    q = [brick]
    removed = []
    while q:
        b = q.pop(0)
        for c in supports[b]:
            supported_by[c].remove(b)
            if len(supported_by[c]) == 0 and c not in q:
                q.append(c)
        removed.append(b)
    return removed

print(sum(len(disintegrate(supported_by, supports, str(i)))-1 for i in range(len(bricks))))
