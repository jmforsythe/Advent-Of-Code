grid = [line.split() for line in open("input.txt").read().splitlines()]
out=0
for j in range(len(grid[0])):
    if grid[-1][j] == "+":
        out += sum(int(grid[i][j]) for i in range(len(grid)-1))
    else:
        prd = 1
        for i in range(len(grid)-1):
            prd *= int(grid[i][j])
        out += prd
print(out)

op_line = open("input.txt").read().splitlines()[-1]
op_pos = [i for i,c in enumerate(op_line) if c != " "]
grid = [[line[a:b-1] for a,b in zip(op_pos, op_pos[1:]+[len(op_line)+1])] for line in open("input.txt").read().splitlines()]
out=0
for j,c in enumerate(grid[-1]):
    op_len = len(c)
    op = c.strip()
    nums = [int("".join([grid[i][j][k] for i in range(len(grid)-1)])) for k in range(op_len-1, -1, -1)]
    if op == "+":
        out += sum(nums)
    else:
        prd = 1
        for n in nums:
            prd *= n
        out += prd
print(out)
