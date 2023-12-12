grid = [list(line.strip()) for line in open("input.txt")]
p = ()
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "S":
            p = (i, j)
n = None
i = p[0]
j = p[1]
if i>0 and grid[i-1][j] in ("|", "7", "F"):
    n = (i-1, j)
elif i < len(grid)-1 and grid[i+1][j] in ("|", "L", "J"):
    n = (i+1, j)
elif j > 0 and grid[i][j-1] in ("-", "L", "F"):
    n = (i, j-1)
elif j < len(grid[i])-1 and grid[i][j+1] in ("-", "J", "7"):
    n = (i, j+1)

def up(x):
    return x, (x[0]-1, x[1])
def right(x):
    return x, (x[0], x[1]+1)
def down(x):
    return x, (x[0]+1, x[1])
def left(x):
    return x, (x[0], x[1]-1)

loop = {p}
while (nc:=grid[n[0]][n[1]]) != "S":
    if p[0] < n[0]:
        # Going down
        match nc:
            case "|": p, n = down(n)
            case "L": p, n = right(n)
            case "J": p, n = left(n)
    elif p[0] > n[0]:
        # Going up
        match nc:
            case "|": p, n = up(n)
            case "7": p, n = left(n)
            case "F": p, n = right(n)
    elif p[1] < n[1]:
        # Going right
        match nc:
            case "-": p, n = right(n)
            case "J": p, n = up(n)
            case "7": p, n = down(n)
    elif p[1] > n[1]:
        # Going left
        match nc:
            case "-": p, n = left(n)
            case "L": p, n = up(n)
            case "F": p, n = down(n)
    loop.add(p)
print((len(loop)+1)//2)
