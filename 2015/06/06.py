import re

lights = set()
lights2 = dict()

for l in open("input.txt").readlines():
    x1,y1,x2,y2 = map(int, re.findall(r"\d+", l))
    a = re.match("turn on", l)
    b = re.match("turn off", l)
    c = re.match("toggle", l)
    for i in range(min(x1,x2), max(x1,x2)+1):
        for j in range(min(y1,y2), max(y1,y2)+1):
            if (i,j) not in lights2:
                lights2[(i,j)] = 0
            if a:
                lights.add((i,j))
                lights2[(i,j)] += 1
            elif b:
                lights.discard((i,j))
                lights2[(i,j)] = max(0, lights2[(i,j)]-1)
            elif c:
                if (i,j) in lights:
                    lights.discard((i,j))
                else:
                    lights.add((i,j))
                lights2[(i,j)] += 2
print(len(lights))
print(sum((v for v in lights2.values() if v>0)))
