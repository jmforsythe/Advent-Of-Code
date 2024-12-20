grid = {i+1j*j: c for i,line in enumerate(open("input.txt").read().splitlines()) for j,c in enumerate(line)}

q = [c for c in grid if grid[c] == "S"]
dist = {q[0]: 0}
for pos in q:
    for d in (1,1j,-1,-1j):
        if pos+d in grid and grid[pos+d] != "#" and pos+d not in dist:
            dist[pos+d] = dist[pos]+1
            q.append(pos+d)

def cheat(max_dist):
    out = 0
    for c in grid:
        if grid[c] == "#":
            continue
        for end in [c+i+1j*j for i in range(-max_dist-1, max_dist+1) for j in range(-max_dist-1, max_dist+1)]:
            if end not in grid or grid[end] == "#":
                continue
            man = int(abs(c.real-end.real)+abs(c.imag-end.imag))
            if man<=1 or man>max_dist:
                continue
            if dist[end]-(dist[c]+man) >= 100:
                out += 1
    return out

print(cheat(2))
print(cheat(20))
