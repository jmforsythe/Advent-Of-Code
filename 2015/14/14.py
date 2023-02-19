import re

LIM = 2503
d = (tuple(map(int, (speed, time, rest))) for line in open("input.txt").readlines() for (speed, time, rest) in [re.match(r".* (\d+).* (\d+).* (\d+)", line).groups()])

print(max((LIM//(time + rest))*speed*time + min(time, LIM%(time + rest))*speed for (speed, time, rest) in d))
