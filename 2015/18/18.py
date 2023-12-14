import itertools

def get_val(i, j, grid):
    return int(i in range(len(grid)) and j in range(len(grid[i])) and grid[i][j])

def run(corners_on):
    grid = []
    for line in open("input.txt").readlines():
        grid.append(list(map(lambda c: int(c == "#"), list(line.strip()))))
    if corners_on:
        grid[0][0] = 1
        grid[0][-1] = 1
        grid[-1][0] = 1
        grid[-1][-1] = 1

    for _ in range(100):
        new_grid = [[0 for col in row] for row in grid]
        for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
            debug = list((get_val(i+k, j+l, grid), i+k, i+l) for k in range(-1,2) for l in range(-1,2))
            num_neighbours = sum(get_val(i+k, j+l, grid) for k in range(-1,2) for l in range(-1,2) if k != 0 or l != 0)
            new_grid[i][j] = int(num_neighbours == 3 or (num_neighbours == 2 and get_val(i, j, grid)))
        grid = new_grid
        if corners_on:
            grid[0][0] = 1
            grid[0][-1] = 1
            grid[-1][0] = 1
            grid[-1][-1] = 1

    print(sum(sum(c for c in l) for l in grid))

run(False)
run(True)
