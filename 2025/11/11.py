g = {}
g["out"] = []
for line in open("input.txt").read().splitlines():
    s, ds = line.split(": ")
    g[s] = ds.split()

from functools import cache

@cache
def count_paths(source, dest):
    if source == dest:
        return 1
    return sum(count_paths(c, dest) for c in g[source])

print(count_paths("you", "out"))
print(count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out") + count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))
