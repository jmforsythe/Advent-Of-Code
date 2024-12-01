pairs = [list(map(int, line.strip().split())) for line in open("input.txt")]
left = [p[0] for p in pairs]
right = [p[1] for p in pairs]
left.sort()
right.sort()
out = 0
right_count = {}
for i in range(len(left)):
    out += abs(left[i]-right[i])
    if right[i] not in right_count:
        right_count[right[i]] = 0
    right_count[right[i]] += 1
out2 = 0
for i in left:
    out2 += i*right_count.get(i, 0)
print(out)
print(out2)
