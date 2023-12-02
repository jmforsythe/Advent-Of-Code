import re

out = 0
power = 0

for line in open("input.txt").readlines():
    l = line.rstrip()
    game_id = l.split(":")[0][5:]
    rounds = l.split(":")[1].split(";")
    possible = True
    dummy = re.match(r"(.)", "0")
    min_red = 0
    min_green = 0
    min_blue = 0
    for round in rounds:
        red = int((re.search(r" (\d+) red", round) or dummy).group(1))
        green = int((re.search(r" (\d+) green", round) or dummy).group(1))
        blue = int((re.search(r" (\d+) blue", round) or dummy).group(1))
        if (red > 12 or green > 13 or blue > 14):
            possible = False
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)
    if possible:
        out += int(game_id)
    power += min_red * min_blue * min_green

print(out)
print(power)
