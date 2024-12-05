p1, p2 = open("input.txt").read().split("\n\n")
mat1 = p1.splitlines()
mat2 = p2.splitlines()
rules = [[False for _ in range(100)] for _ in range(100)]
for l in mat1:
    a, b = l.split("|")
    rules[int(a)][int(b)] = True

out = 0
out2 = 0
for l in mat2:
    pages = [int(a) for a in l.split(",")]
    valid = all(rules[pages[j]][pages[i]] == False for i in range(len(pages)) for j in range(i+1, len(pages)))
    if valid:
        out += pages[len(pages)//2]
    else:
        for i in range(len(pages)):
            for j in range(len(pages)):
                if rules[pages[i]][pages[j]]:
                    pages[i], pages[j] = pages[j], pages[i]
        out2 += pages[len(pages)//2]
print(out)
print(out2)
