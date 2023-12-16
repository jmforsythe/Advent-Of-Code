grid = [list(line.strip()) for line in open("input.txt")]

activated = set()
activated_with_dir = set()
def simulate(pos, dir):
    if (pos, dir) in activated_with_dir:
        return None, False
    if pos[0] not in range(len(grid)) or pos[1] not in range(len(grid[0])):
        return None, False
    activated.add(pos)
    activated_with_dir.add((pos, dir))
    c = grid[pos[0]][pos[1]]
    split = False
    match c:
        case "/":
            match dir:
                case (1,0): dir = (0,-1)
                case (0,1): dir = (-1,0)
                case (-1,0): dir = (0,1)
                case (0,-1): dir = (1,0)
        case "\\":
            match dir:
                case (1,0): dir = (0,1)
                case (0,1): dir = (1,0)
                case (-1,0): dir = (0,-1)
                case (0,-1): dir = (-1,0)
        case "|":
            if dir[1] != 0:
                dir = (1,0)
                split = True
        case "-":
            if dir[0] != 0:
                dir = (0,1)
                split = True
    return dir, split

def run(initial_pos, initial_dir):
    activated.clear()
    activated_with_dir.clear()

    beams = [(initial_pos, initial_dir)]

    while len(beams):
        to_remove = []
        for i, (pos, dir) in enumerate(beams):
            new_dir, split = simulate(pos, dir)
            if new_dir == None:
                to_remove.append((pos, dir))
            else:
                beams[i] = ((pos[0]+new_dir[0], pos[1]+new_dir[1]), new_dir)
            if split:
                beams.append(((pos[0]-new_dir[0], pos[1]-new_dir[1]), (-new_dir[0], -new_dir[1])))
        for beam in to_remove:
            beams.remove(beam)
    return len(activated)

out = run((0,0), (0,1))
print(out)

for i in range(1, len(grid)):
    out = max(out, run((i,0), (0,1)))
for i in range(len(grid)):
    out = max(out, run((i,len(grid[0])-1), (0,-1)))
for j in range(len(grid[0])):
    out = max(out, run((0,j), (1,0)))
for j in range(len(grid[0])):
    out = max(out, run((len(grid)-1,j), (-1,0)))

print(out)
