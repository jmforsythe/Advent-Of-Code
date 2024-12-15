lines = open("input.txt").read().splitlines()
grid = {i+j*1j: c for i,line in enumerate(lines[:lines.index("")]) for j,c in enumerate(line)}
instructions = "".join(lines[lines.index(""):])
pos = [key for key in grid if grid[key] == "@"][0]
grid[pos] = "."

def print_grid(mult=1):
    for i in range(lines.index("")):
        s = ""
        for j in range(len(lines[0])*mult):
            s += grid[i+j*1j] if pos != i+j*1j else "@"
        print(s)
    print()

for i in instructions:
    d = {">": 1j, "v": 1, "<": -1j, "^": -1}[i]
    dest = pos+d
    while grid[dest] == "O":
        dest += d
    if grid[dest] == "#":
        continue
    grid[dest] = grid[pos+d]
    pos += d

print(sum(100*int(p.real)+int(p.imag) for p in grid if grid[p] == "O"))

grid = {i+j*2j: c for i,line in enumerate(lines[:lines.index("")]) for j,c in enumerate(line)}
pos = [key for key in grid if grid[key] == "@"][0]
grid[pos] = "."
for key in list(grid.keys()):
    neighbour = key + 1j
    grid[neighbour] = grid[key]
    if grid[key] == "O":
        grid[key] = "["
        grid[neighbour] = "]"

for i in instructions:
    d = {">": 1j, "v": 1, "<": -1j, "^": -1}[i]
    if d.real:
        stopped = False
        to_move = [pos+d]
        for dest in to_move:
            if grid[dest] == "#":
                stopped = True
                break
            if grid[dest] == "[":
                if dest+1j not in to_move:
                    to_move.append(dest+1j)
                to_move.append(dest+d)
            elif grid[dest] == "]":
                if dest-1j not in to_move:
                    to_move.append(dest-1j)
                to_move.append(dest+d)
        if not stopped:
            for dest in to_move[::-1]:
                grid[dest] = grid[dest-d] if dest-d in to_move else "."
            pos += d
    else:
        dest = pos+d
        while grid[dest] in ("[","]"):
            dest += d
        if grid[dest] == "#":
            continue
        while dest != pos:
            grid[dest] = grid[dest-d]
            dest -= d
        pos += d

print(sum(100*int(p.real)+int(p.imag) for p in grid if grid[p] == "["))
