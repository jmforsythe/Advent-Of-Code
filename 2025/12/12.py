lines = open("input.txt").read().splitlines()
NUM_SHAPES = 6
shapes = [lines[5*i+1:5*i+4] for i in range(NUM_SHAPES)]

yes = 0
maybe = 0

areas = [sum(sum(c == "#" for c in row) for row in shape) for shape in shapes]
for line in lines[30:]:
    a, b = line.split(": ")
    w, h = list(map(int, a.split("x")))
    area = w*h
    counts = [int(i) for i in b.split()]
    needed_area = sum(areas[i]*counts[i] for i in range(NUM_SHAPES))
    if (w//3) * (h//3) >= sum(counts):
        yes += 1
    elif area >= needed_area:
        maybe += 1

print(yes, maybe)
