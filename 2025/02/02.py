out=0
invalids = set()
for pair in open("input.txt").read().strip().split(","):
    a,b = pair.split("-")
    for r in range(2,len(b)+1):
        start = int(a[:len(a)//r] or 0)
        end = int(b[:(len(b)+(r-1))//r])
        for i in range(start, end+1):
            id = int("".join(str(i) for _ in range(r)))
            if id in range(int(a), int(b)+1):
                if r==2:
                    out += id
                invalids.add(id)
print(out)
print(sum(invalids))
