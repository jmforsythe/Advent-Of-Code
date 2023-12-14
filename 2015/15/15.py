import math
import functools

inp = [tuple(int(val) for key, val in [pair.split() for pair in data.split(", ")]) for line in open("input.txt").readlines() for name, data in (line.rstrip().split(": "),)]

TOTAL = 100

def add(l, t):
    for i in range(len(l)):
        l[i] += t[i]

def value(l):
    prod = 1
    for i in range(len(l)-1):
        prod *= max(0, l[i])
    return prod

def main(calorie_restrict):
    best = 0
    current = [0,0,0,0,0]
    for frosting in range(TOTAL+1):
        before_candy = [i for i in current]
        for candy in range(TOTAL-(frosting)+1):
            before_butterscotch = [i for i in current]
            for butterscotch in range(TOTAL-(frosting+candy)+1):
                before_sugar = [i for i in current]
                for sugar in range(TOTAL-(frosting+candy+butterscotch)+1):
                    v = value(current)
                    if v > best and (calorie_restrict == None or calorie_restrict == current[-1]):
                        best = v
                    add(current, inp[3])
                current = before_sugar
                add(current, inp[2])
            current = before_butterscotch
            add(current, inp[1])
        current = before_candy
        add(current, inp[0])
    return best

print(main(None))
print(main(500))
