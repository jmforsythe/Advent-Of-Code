lines = open("input.txt").readlines()

seeds = [int(i) for i in lines[0].rstrip().split(": ")[1].split()]
new_seeds = [seed for seed in seeds]

for line in lines:
    if line == "\n":
        seeds = [seed for seed in new_seeds]
    if not line[0].isdecimal():
        continue
    dest_start, source_start, length = [int(i) for i in line.rstrip().split()]
    for i, seed in enumerate(seeds):
        if seed in range(source_start, source_start+length):
            dest = dest_start + seed-source_start
            new_seeds[i] = dest
seeds = [seed for seed in new_seeds]
print(min(seeds))

seeds = [int(i) for i in lines[0].rstrip().split(": ")[1].split()]
seed_ranges = [range(a, a+b) for a,b in zip(seeds[0::2], seeds[1::2])]

start_location = -1
while True:
    start_location += 1
    location = start_location
    isSet = False
    for line in lines[::-1]:
        if line == "\n":
            isSet = False
        if isSet or not line[0].isdigit():
            continue
        dest_start, source_start, length = [int(i) for i in line.rstrip().split()]
        if location in range(dest_start, dest_start+length):
            location = source_start + location-dest_start
            isSet = True
    if any(location in r for r in seed_ranges):
        print(start_location)
        break
