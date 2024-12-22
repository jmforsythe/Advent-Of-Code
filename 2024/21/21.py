grid_num = [["7","8","9"],["4","5","6"],["1","2","3"],["_","0","A"]]
coords_num = {c: (i,j) for i,l in enumerate(grid_num) for j,c in enumerate(l)}

def paths_between_nums(num1, num2):
    c1 = coords_num[num1]
    c2 = coords_num[num2]
    vertical = "^"*(c1[0]-c2[0])+"v"*(c2[0]-c1[0])
    horizontal = "<"*(c1[1]-c2[1])+">"*(c2[1]-c1[1])
    if c1[0]==3 and c2[1]==0:
        return [vertical+horizontal]
    if c1[1]==0 and c2[0]==3:
        return [horizontal+vertical]
    return list(set([vertical+horizontal, horizontal+vertical]))

grid_dir = [["_","^","A"],["<","v",">"]]
coords_dir = {c: (i,j) for i,l in enumerate(grid_dir) for j,c in enumerate(l)}

def paths_between_dirs(dir1, dir2):
    c1 = coords_dir[dir1]
    c2 = coords_dir[dir2]
    vertical = "^"*(c1[0]-c2[0])+"v"*(c2[0]-c1[0])
    horizontal = "<"*(c1[1]-c2[1])+">"*(c2[1]-c1[1])
    if c1[0]==0 and c2[1]==0:
        return [vertical+horizontal]
    if c1[1]==0 and c2[0]==0:
        return [horizontal+vertical]
    return list(set([vertical+horizontal, horizontal+vertical]))

from functools import cache
@cache
def num_moves(start, end, layer, top_layer):
    grid = grid_num if layer == 0 else grid_dir
    coords = coords_num if layer == 0 else coords_dir
    if start == end:
        return 1
    c1 = coords[start]
    c2 = coords[end]
    if layer == top_layer-1:
        return abs(c1[0]-c2[0])+abs(c1[1]-c2[1])+1
    candidates = []
    possibilities = paths_between_nums(start, end) if layer == 0 else paths_between_dirs(start, end)
    for pos in possibilities:
        steps = num_moves("A", pos[0], layer+1, top_layer)
        for i in range(len(pos)-1):
            steps += num_moves(pos[i], pos[i+1], layer+1, top_layer)
        steps += num_moves(pos[-1], "A", layer+1, top_layer)
        candidates.append(steps)
    return min(candidates)

for depth in [2, 25]:
    out = 0
    for line in open("input.txt").read().splitlines():
        complexity = num_moves("A", line[0], 0, depth+1)
        for i in range(len(line)-1):
            complexity += num_moves(line[i], line[i+1], 0, depth+1)
        out += complexity * int(line[:-1])
    print(out)
