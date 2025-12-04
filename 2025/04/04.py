lines = [[c for c in l] for l in open("input.txt").read().splitlines()]
find_open = lambda lines : [[int(lines[i][j]=="@" and sum(lines[a][b]=="@" for a in range(max(0, i-1), min(len(lines), i+1+1)) for b in range(max(0, j-1), min(len(lines[0]), j+1+1)))<5) for j in range(len(lines[i]))] for i in range(len(lines))]
num_open = lambda o: sum(sum(row) for row in o)
print(num_open(find_open(lines)))
out2 = 0
while num_open(o := find_open(lines)) > 0:
    out2 += num_open(o)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if o[i][j]:
                lines[i][j] = "."
print(out2)
