S = 70
grid = {i+1j*j: "." for i in range(S+1) for j in range(S+1)}
for line in open("input.txt").read().splitlines()[:1024]:
    i,j = line.split(",")
    grid[int(i)+1j*int(j)] = "#"

def solve():
    q = [(0,0)]
    seen = {0}
    while q:
        dist, pos = q.pop(0)
        if pos == S+1j*S:
            return dist
        for d in (1,1j,-1,-1j):
            if pos+d in grid and grid[pos+d] == "." and pos+d not in seen:
                seen.add(pos+d)
                q.append((dist+1, pos+d))
    return -1

print(solve())
for line in open("input.txt").read().splitlines()[1024:]:
    i,j = line.split(",")
    grid[int(i)+1j*int(j)] = "#"
    if solve() == -1:
        print(f"{i},{j}")
        break
