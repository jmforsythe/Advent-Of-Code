grid = [list(line.strip()) for line in open("input.txt")]

def rotate_180(grid):
    return [row[::-1] for row in grid][::-1]

def rotate_anticlockwise(grid):
    return [[row[-i-1] for row in grid] for i in range(len(grid[0]))]

def rotate_clockwise(grid):
    return rotate_180(rotate_anticlockwise(grid))

def pg(grid):
    for r in grid:
        print("".join(r))
    print()

def tilt_left(g):
    grid = [[c for c in r] for r in g]
    for i, row in enumerate(grid):
        square_pos = [0] + [i for i, x in enumerate(row) if x == "#"] + [len(row)]
        for start, end in zip(square_pos, square_pos[1:]):
            row = row[:start] + sorted(row[start:end], key=lambda x: ["#", "O", "."].index(x)) + row[end:]
        grid[i] = row
    return grid

def stress(grid):
    out = 0
    for row in rotate_anticlockwise(grid):
        for i, x in enumerate(reversed(row)):
            if x == "O":
                out += i + 1
    return out

print(stress(rotate_clockwise(tilt_left(rotate_anticlockwise(grid)))))

states = []
stresses = []
cycle_start = -1

while True:
    grid = rotate_clockwise(tilt_left(rotate_anticlockwise(grid))) # North
    grid = tilt_left(grid) # West
    grid = rotate_anticlockwise(tilt_left(rotate_clockwise(grid))) # South
    grid = rotate_180(tilt_left(rotate_180(grid))) # East
    state = tuple(tuple(row) for row in grid)
    if hash(state) in states:
        cycle_start = states.index(hash(state))
        break
    states.append(hash(state))
    stresses.append(stress(grid))

rem = (1_000_000_000-1-cycle_start) % (len(states) - cycle_start)

print(stresses[cycle_start + rem])