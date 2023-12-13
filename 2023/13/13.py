def symmetries(rep):
    return [i for i in range(len(rep)-1) if all(p == q for p, q in zip(rep[i::-1], rep[i+1:]))]

def grid_symmetries(grid):
    m = dict()
    m2 = dict()
    for i, line in enumerate(grid):
        if tuple(line) not in m:
            m[tuple(line)] = []
        m[tuple(line)].append(i)
    for j in range(len(grid[0])):
        column = [row[j] for row in grid]
        if tuple(column) not in m2:
            m2[tuple(column)] = []
        m2[tuple(column)].append(j)
    rep = [0 for _ in grid]
    rep2 = [0 for _ in grid[0]]
    for i, k in enumerate(m):
        v = m[k]
        for j in v:
            rep[j] = i
    for i, k in enumerate(m2):
        v = m2[k]
        for j in v:
            rep2[j] = i
    return (symmetries(rep), symmetries(rep2))

grids = []
grid = []
for line in open("input.txt"):
    if line.strip() == "":
        grids.append(grid)
        grid = []
        continue
    grid.append(line.strip())
grids.append(grid)

out = 0
out2 = 0

for grid_num, grid in enumerate(grids):
    s1, s2 = grid_symmetries(grid)
    for s in s1:
        out += 100 * (s+1)
    for s in s2:
        out += s+1
    t1s = set()
    t2s = set()
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            new_grid = [row for row in grid]
            new_grid[i] = new_grid[i][:j] + ("#" if c == "." else ".") + new_grid[i][j+1:]
            t1, t2 = grid_symmetries(new_grid)
            for t in t1:
                if t not in s1:
                    t1s.add(t)
            for t in t2:
                if t not in s2:
                    t2s.add(t)
            continue
    for t in t1s:
        out2 += 100 * (t+1)
    for t in t2s:
        out2 += t+1

print(out)
print(out2)
