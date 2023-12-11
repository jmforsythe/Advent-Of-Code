ins = open("input.txt").readline().strip()

m = {}
for line in open("input.txt").readlines()[2:]:
    a, b = line.strip().split(" = ")
    m[a] = (b[1:4], b[6:9])

pos = "AAA"
num = 0
while True:
    i = ins[num % len(ins)]
    num += 1
    if pos == "ZZZ":
        print(num)
        break
    pos = m[pos][0 if i == "L" else 1 if i == "R" else None]

pos_arr = [p for p in m if p[-1] == "A"]
time_to_z = [-1 for p in pos_arr]
num = 0
while any(t == -1 for t in time_to_z):
    i = ins[num % len(ins)]
    num += 1
    for ind, p in enumerate(pos_arr):
        if time_to_z[ind] == -1:
            pos_arr[ind] = m[p][0 if i == "L" else 1 if i == "R" else None]
            if pos_arr[ind][-1] == "Z":
                time_to_z[ind] = num

import math

print(math.lcm(*time_to_z))