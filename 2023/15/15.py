from functools import reduce

def hash(string):
    return reduce(lambda o, c: ((o+ord(c))*17)%256, string, 0)

boxes = [[] for _ in range(256)]

out = 0
for s in open("input.txt").read().replace("\n", "").split(","):
    out += hash(s)

    if "=" in s:
        label, num = s.split("=")
        insert = True
        for i, p in enumerate(boxes[hash(label)]):
            if p[0] == label:
                boxes[hash(label)][i] = ((label, int(num)))
                insert = False
                break
        if insert:
            boxes[hash(label)].append((label, int(num)))
    else:
        label = s.rstrip("-")
        for p in boxes[hash(label)]:
            if p[0] == label:
                boxes[hash(label)].remove(p)
                break
print(out)

print(sum((i+1)*(j+1)*num for i, box in enumerate(boxes) for j, (label, num) in enumerate(box)))

