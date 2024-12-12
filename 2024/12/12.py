mat = open("input.txt").read().splitlines()
board = {}
seen = set()

out = 0
out2 = 0

for x in range(len(mat)):
    for y in range(len(mat[0])):
        if (x,y) in seen:
            continue
        perimeter = 0
        area = 0
        sides = 0
        s = [(x,y)]
        seen.add((x,y))
        while s:
            i,j = s.pop()
            area += 1
            outside = [0,0,0,0]
            for n, (a,b) in enumerate(((i+1,j),(i,j+1),(i-1,j),(i,j-1))):
                if a in range(len(mat)) and b in range(len(mat[0])) and mat[i][j]==mat[a][b]:
                    if (a,b) not in seen:
                        s.append((a,b))
                        seen.add((a,b))
                else:
                    outside[n] = 1
                    perimeter += 1
            for n in range(4):
                if outside[n] and outside[(n+1)%4]:
                    sides += 1
            if outside[0] + outside[1] == 0:
                sides += mat[i+1][j+1] != mat[i][j]
            if outside[1] + outside[2] == 0:
                sides += mat[i-1][j+1] != mat[i][j]
            if outside[2] + outside[3] == 0:
                sides += mat[i-1][j-1] != mat[i][j]
            if outside[3] + outside[0] == 0:
                sides += mat[i+1][j-1] != mat[i][j]    
        out += area * perimeter
        out2 += area * sides

print(out)
print(out2)
