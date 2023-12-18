pos = (0,0)
pos2 = (0,0)
corners1 = [pos]
corners2 = [pos2]
for line in open("input.txt"):
    d, s, c = line.strip().split()
    match d:
        case "R": pos = (pos[0], pos[1]+int(s))
        case "D": pos = (pos[0]+int(s), pos[1])
        case "L": pos = (pos[0], pos[1]-int(s))
        case "U": pos = (pos[0]-int(s), pos[1])
    corners1.append(pos)

    step_size = int(c[2:-2], 16)
    match c[-2]:
        case "0": pos2 = (pos2[0], pos2[1]+step_size)
        case "1": pos2 = (pos2[0]+step_size, pos2[1])
        case "2": pos2 = (pos2[0], pos2[1]-step_size)
        case "3": pos2 = (pos2[0]-step_size, pos2[1])
    corners2.append(pos2)

def area(corners):
    extra = 0
    for p, q in zip(corners, corners[1:]+[corners[0]]):
        if p[0] == q[0]:
            extra += abs(p[1]-q[1])
        elif p[1] == q[1]:
            extra += abs(p[0]-q[0])
    return 1+(extra + abs(sum(p[0]*q[1] - p[1]*q[0] for p, q in zip(corners, corners[1:]))))//2

print(area(corners1))
print(area(corners2))
