grid = [list(line.strip()) for line in open("input.txt")]

rows_to_double = [i for i, line in enumerate(grid) if all(c == "." for c in line)]
cols_to_double = [i for i in range(len(grid[0])) if all(row[i] == "." for row in grid)]
galaxies = [(i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "#"]

out = 0
out2 = 0
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies[i:]):
        min_i = min(g1[0], g2[0])
        min_j = min(g1[1], g2[1])
        max_i = max(g1[0], g2[0])
        max_j = max(g1[1], g2[1])
        dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        row_extra = len([r for r in rows_to_double if r in range(min_i, max_i)])
        col_extra = len([c for c in cols_to_double if c in range(min_j, max_j)])
        out += dist + row_extra + col_extra
        out2 += dist + (1000000-1) * (row_extra + col_extra)
print(out)
print(out2)
