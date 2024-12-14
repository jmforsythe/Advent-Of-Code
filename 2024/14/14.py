import re
dat = re.findall(r"p=(.+),(.+) v=(.*),(.*)", open("input.txt").read())
points = [(int(d[0])+1j*int(d[1]), int(d[2])+1j*int(d[3])) for d in dat]

width = 101
midw = width//2
height = 103
midh = height//2

quads = [0,0,0,0]
for i, (p,v) in enumerate(points):
    p += 100*v
    p = (p.real % width) + (1j * (p.imag % height))
    if p.real < midw and p.imag < midh:
        quads[0] += 1
    elif p.real < midw and p.imag > midh:
        quads[1] += 1
    elif p.real > midw and p.imag < midh:
        quads[2] += 1
    elif p.real > midw and p.imag > midh:
        quads[3] += 1

def print_grid():
    s = ""
    for j in range(height):
        for i in range(width):
            s += str(sum(p[0] == i+1j*j for p in points) or ".") + " "
        s += "\n"
    print(s)
    print()
    print()

fewest_rows = (-1, len(points))
fewest_cols = (-1, len(points))

for _ in range(max(width, height)+1):
    rows = set()
    cols = set()
    for i, (p,v) in enumerate(points):
        p += v
        p = (p.real % width) + (1j * (p.imag % height))
        points[i] = (p,v)
        rows.add(int(p.imag))
        cols.add(int(p.real))
    if len(cols) < fewest_cols[1]:
        fewest_cols = (_, len(cols))
    if len(rows) < fewest_rows[1]:
        fewest_rows = (_, len(rows))

points = [(int(d[0])+1j*int(d[1]), int(d[2])+1j*int(d[3])) for d in dat]
j = fewest_cols[0]+1
while j%103 != fewest_rows[0]+1:
    j += 101
for i, (p,v) in enumerate(points):
    p += j*v
    p = (p.real % width) + (1j * (p.imag % height))
    points[i] = (p,v)
print_grid()
print(j)
