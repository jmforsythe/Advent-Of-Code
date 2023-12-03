rows = open("input.txt").readlines()

symbols = []
stars = []

for y, row in enumerate(rows):
    for x, val in enumerate(row.rstrip()):
        if not val.isdecimal() and val != ".":
            symbols.append((x,y))
            if val == "*":
                stars.append((x,y))

star_numbers = [[] for star in stars]

out = 0

for y, row in enumerate(rows):
    row = row.rstrip()
    inNumber = False
    num_pos = [x for (x, val) in enumerate(row) if val.isdecimal()]
    ranges = []
    cur_start = None
    prev = None
    cur_end = None
    for pos in num_pos:
        if prev == None:
            cur_start = pos
            cur_end = pos
        elif pos == prev+1:
            cur_end = pos
        else:
            ranges.append((cur_start, cur_end))
            cur_start = pos
            cur_end = pos
        prev = pos
    if cur_start != None and cur_end != None:
        ranges.append((cur_start, cur_end))
    for r in ranges:
        added = False
        for x in range(r[0]-1, r[1]+2):
            if (x,y) in symbols or (x,y-1) in symbols or (x,y+1) in symbols:
                number = int(row[r[0]:r[1]+1])
                added = True
                if added:
                    out += number
            if (x,y) in stars:
                star_numbers[stars.index((x,y))].append(number)
            if (x,y-1) in stars:
                star_numbers[stars.index((x,y-1))].append(number)
            if (x,y+1) in stars:
                star_numbers[stars.index((x,y+1))].append(number)

print(out)

print(sum(star_numbers[i][0] * star_numbers[i][1] for i in range(len(stars)) if len(star_numbers[i]) == 2))
