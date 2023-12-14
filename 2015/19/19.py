import re

m = {}
for line in open("input.txt").readlines():
    if line.strip() == "":
        break
    key, val = line.strip().split(" => ")
    if key not in m:
        m[key] = []
    m[key].append(val)

big_string = open("input.txt").readlines()[-1].strip()

out = set()

for key, val in m.items():
    for x in re.finditer(key, big_string):
        start, end = x.span()
        for v in val:
            out.add(big_string[:start] + v + big_string[end:])

print(len(out))

seen = set()
cur = set()
next = set("e")

i = 0
while True:
    i += 1
    cur = next
    next = set()
    print(f"{i=}, {len(cur)=}")
    for t in cur:
        if t == big_string:
            exit()
        for key, val in m.items():
            for x in re.finditer(key, t):
                start, end = x.span()
                for v in val:
                    pos_val = t[:start] + v + t[end:]
                    if pos_val not in seen:
                        seen.add(pos_val)
                        next.add(pos_val)
