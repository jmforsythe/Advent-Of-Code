out = 0
copies = [1 for i in open("input.txt").readlines()]
print(len(copies))
for i, line in enumerate(open("input.txt").readlines()):
    a, b = line.rstrip().split(": ")[1].split(" | ")
    win = tuple(int(num) for num in a.split())
    have = tuple(int(num) for num in b.split())
    num_winning = 0
    for num in win:
        if num in have:
            num_winning += 1
    for j in range(i+1, min(len(copies), i+1+num_winning)):
        copies[j] += copies[i]
    if num_winning > 0:
        out += 2**(num_winning-1)
print(out)
print(sum(copies))
