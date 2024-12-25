lines = open("input.txt").read().splitlines()
grids = [lines[i:i+7] for i in range(0,len(lines),8)]
locks = []
keys = []
for grid in grids:
    nums = [sum(grid[i][j] == "#" for i in range(len(grid)))-1 for j in range(len(grid[0]))]
    if grid[0][0] == "#":
        locks.append(nums)
    else:
        keys.append(nums)
out = 0
for lock in locks:
    for key in keys:
        out += all(lock[i]+key[i]<=5 for i in range(len(lock)))
print(out)
