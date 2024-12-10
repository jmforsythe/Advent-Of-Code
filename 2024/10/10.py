mat = {i+j*1j: int(c) for i, line in enumerate(open("input.txt").read().splitlines()) for j, c in enumerate(line)}
reachable = {}
paths = {}
for pos in {pos for pos in mat if mat[pos] == 9}:
    reachable[pos] = set([pos])
    paths[pos] = [[pos]]
for n in range(8,-1,-1):
    for pos in {pos for pos in mat if mat[pos] == n}:
        reachable[pos] = {r for d in (1+0j, 0+1j, -1+0j, 0-1j) if pos+d in reachable and mat[pos+d] == n+1 for r in reachable[pos+d]}
        paths[pos] = [path + [pos] for d in (1+0j, 0+1j, -1+0j, 0-1j) if pos+d in paths and mat[pos+d] == n+1 for path in paths[pos+d]]
print(sum(len(reachable[pos]) for pos in {pos for pos in mat if mat[pos] == 0}))
print(sum(len(paths[pos]) for pos in {pos for pos in mat if mat[pos] == 0}))
