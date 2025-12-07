grid = open("input.txt").read().splitlines()
beams = {grid[0].index("S"): 1}
out=0
for line in grid[1:]:
    beams_next = {}
    for b in beams:
        if line[b] == ".":
            if b not in beams_next:
                beams_next[b] = 0
            beams_next[b] += beams[b]
        elif line[b] == "^":
            out += 1
            if b-1 not in beams_next:
                beams_next[b-1] = 0
            beams_next[b-1] += beams[b]
            if b+1 not in beams_next:
                beams_next[b+1] = 0
            beams_next[b+1] += beams[b]
    beams = beams_next
print(out)
print(sum(beams.values()))
