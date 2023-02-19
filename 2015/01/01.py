l = open("input.txt").read()
floor = 0
part2 = None
for i, c in enumerate(l):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    if floor == -1 and part2 == None:
        part2 = i+1
print(floor)
print(part2)
