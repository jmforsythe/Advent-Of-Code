grid = open("input.txt").read().splitlines()
m = len(grid)
n = len(grid[0])

UP = 0+1j
RIGHT = 1+0j
DOWN = 0-1j
LEFT = -1+0j
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

num_left = [[int(grid[i][j]=="#") for j in range(n)] for i in range(m)]
num_above = [[int(grid[i][j]=="#") for i in range(m)] for j in range(n)]
for i in range(m):
    for j in range(1, n):
        num_left[i][j] += num_left[i][j-1]
for j in range(n):
    for i in range(1, m):
        num_above[j][i] += num_above[j][i-1]

from bisect import bisect_left, bisect_right
def fire(pos, direction):
    i, j = pos
    if direction == RIGHT:
        j = bisect_right(num_left[pos[0]], num_left[pos[0]][pos[1]])
    if direction == LEFT:
        if num_left[pos[0]][pos[1]] == 0:
            j = -1
        else:
            j = bisect_left(num_left[pos[0]], num_left[pos[0]][pos[1]])
    if direction == UP:
        if num_above[pos[1]][pos[0]] == 0:
            i = -1
        else:
            i = bisect_left(num_above[pos[1]], num_above[pos[1]][pos[0]])
    if direction == DOWN:
        i = bisect_right(num_above[pos[1]], num_above[pos[1]][pos[0]])
    return (i,j)

def get_path(pos, start_direction, seen=set()):
    if (pos, start_direction) in seen:
        return [pos, -1]
    end_point = fire(pos, start_direction)
    if end_point[0] not in range(m) or end_point[1] not in range(n):
        return [pos, end_point]
    one_away = (end_point[0]-int(-start_direction.imag), end_point[1]-int(start_direction.real))
    return [pos] + get_path(one_away, start_direction*(0-1j), seen | {(pos, start_direction)})

start = (-1,-1)
d = 0+0j
for i in range(m):
    for j in range(n):
        if grid[i][j] in ("^",">","v","<"):
            start = (i, j)
            d = DIRECTIONS[("^",">","v","<").index(grid[i][j])]

path = get_path(start, d)

seen = set()
for i in range(1, len(path)):
    a_step = 1 if path[i-1][0]<path[i][0]+1 else -1
    b_step = 1 if path[i-1][1]<path[i][1]+1 else -1
    for a in range(path[i-1][0], path[i][0]+a_step, a_step):
        for b in range(path[i-1][1], path[i][1]+b_step, b_step):
            if a in range(m) and b in range(n):
                seen.add((a,b))
print(len(seen))

out = 0
for i,j in seen:
    for a in range(j, len(num_left[i])):
        num_left[i][a] += 1
    for a in range(i, len(num_above[j])):
        num_above[j][a] += 1
    out += get_path(start, d)[-1] == -1
    for a in range(j, len(num_left[i])):
        num_left[i][a] -= 1
    for a in range(i, len(num_above[j])):
        num_above[j][a] -= 1
print(out)
