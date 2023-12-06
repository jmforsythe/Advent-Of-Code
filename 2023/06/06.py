with open("input.txt") as f:
    times = list(map(int, next(f).split(":")[1].strip().split()))
    distances = list(map(int, next(f).split(":")[1].strip().split()))

p = list(zip(times,distances))

out = 1

for t, d in p:
    discrim = t**2 - 4*d
    x1 = (t - discrim ** 0.5)/2
    x2 = (t + discrim ** 0.5)/2
    num = min(int(x2-0.00001), t) - max(int(x1)+1, 0)+1
    out *= num

print(out)

t = int("".join(map(str, times)))
d = int("".join(map(str, distances)))

discrim = t**2 - 4*d
x1 = (t - discrim ** 0.5)/2
x2 = (t + discrim ** 0.5)/2
print(min(int(x2-0.00001), t) - max(int(x1)+1, 0)+1)
