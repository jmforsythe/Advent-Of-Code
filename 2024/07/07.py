d = [(int(a), [int(c) for c in b.split()]) for a,b in [line.split(": ") for line in open("input.txt").read().splitlines()]]
out = 0
for target, nums in d:
    possible = [nums[0]]
    for i in nums[1:]:
        possible = [a+i for a in possible] + [a*i for a in possible]
    if target in possible:
        out += target
print(out)
out = 0
for target, nums in d:
    possible = [nums[0]]
    for i in nums[1:]:
        possible = [a+i for a in possible] + [a*i for a in possible] + [int(str(a)+str(i)) for a in possible]
    if target in possible:
        out += target
print(out)
