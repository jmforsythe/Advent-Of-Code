mat = open("input.txt").read().splitlines()
d = {c: [(i, j) for i in range(len(mat)) for j in range(len(mat)) if mat[i][j] == c] for c in set(c for line in mat for c in line) if c != "."}
print(len({(i+(i-a), j+(j-b)) for c in d for a,b in d[c] for i,j in d[c] if (i,j) != (a,b) and i+(i-a) in range(len(mat)) and j+(j-b) in range(len(mat[0]))}))
print(len({(x, y) for c in d for a, b in d[c] for i, j in d[c] if (a, b) != (i, j) for x, y in zip(range(i, len(mat) if i-a > 0 else -1, i-a), range(j, len(mat[0]) if j-b > 0 else -1, j-b))}))
