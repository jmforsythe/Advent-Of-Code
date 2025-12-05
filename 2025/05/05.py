from bisect import bisect_left

lines = open("input.txt").read().splitlines()
ranges = sorted([tuple(map(int, line.split("-"))) for line in lines[:lines.index("")]])
merged_ranges = [ranges[0]]
for a,b in ranges[1:]:
    if a <= merged_ranges[-1][1]:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], b))
    else:
        merged_ranges.append((a,b))
out = 0
for id in lines[lines.index("")+1:]:
    pos = bisect_left(merged_ranges, (int(id),int(id)))
    if pos==0:
        continue
    if int(id) >= merged_ranges[pos-1][0] and int(id) <= merged_ranges[pos-1][1]:
        out += 1
print(out)
print(sum(b-a+1 for a,b in merged_ranges))
