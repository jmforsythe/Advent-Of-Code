grid = [list(line.strip()) for line in open("input.txt")]

s_pos = None

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "S":
            s_pos = (i, j)

def run(q):
    q = set(q)
    q2 = set()
    while q:
        i, j = q.pop()
        for a in (-1, 1):
            if i+a in range(len(grid)) and grid[i+a][j] in (".", "S"):
                q2.add((i+a, j))
        for b in (-1, 1):
            if j+b in range(len(grid[0])) and grid[i][j+b] in (".", "S"):
                q2.add((i, j+b))
    return q2

q = {s_pos}
for _ in range(64):
    q = run(tuple(q))
q_64 = q
print(len(q_64))
q_65 = run(tuple(q_64))

assert(len(grid) == 131 and len(grid[0]) == 131 and s_pos == (65, 65))
n = (26501365 - 65) // 131

q = {s_pos}
for _ in range(130):
    q = run(tuple(q))
evens = q
odds = run(tuple(q))

print(len(odds)*(n+1)**2 + len(evens)*n**2 - (n+1)*len(odds-q_65) + n*len(evens-q_64) - n)
