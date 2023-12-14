import re

LIM = 2503
d = tuple(tuple(map(int, (speed, time, rest))) for line in open("input.txt").readlines() for (speed, time, rest) in [re.match(r".* (\d+).* (\d+).* (\d+)", line).groups()])

print(max((LIM//(time + rest))*speed*time + min(time, LIM%(time + rest))*speed for (speed, time, rest) in d))

cur_pos = [0 for _ in d]
scores = [0 for _ in d]
for num_sec in range(LIM):
    for i, r in enumerate(d):
        if num_sec % (r[1]+r[2]) < r[1]:
            cur_pos[i] += r[0]
    m = max(cur_pos)
    for i, p in enumerate(cur_pos):
        if cur_pos[i] == m:
            scores[i] += 1
print(max(scores))
