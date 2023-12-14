def sues():
    for line in open("input.txt", "r").readlines():
        yield {key: int(val) for key, val in (pair.split(": ") for pair in line.rstrip().split(": ", 1)[1].split(", "))}

MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for i, sue in enumerate(sues(), 1):
    if all(sue[key] == MFCSAM[key] for key in sue):
        print(i)
        break

GREATER_THAN_KEYS = ("cats", "trees")
LESS_THAN_KEYS = ("pomeranians", "goldfish")

def part2(sue):
    for key in sue:
        if key in GREATER_THAN_KEYS:
            if not sue[key] > MFCSAM[key]:
                return False
        elif key in LESS_THAN_KEYS:
            if not sue[key] < MFCSAM[key]:
                return False
        else:
            if not sue[key] == MFCSAM[key]:
                return False
    return True

for i, sue in enumerate(sues(), 1):
    if part2(sue):
        print(i)
        break
