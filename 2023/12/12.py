from functools import cache

@cache
def num_ways(chars, contig):
    chars = chars.lstrip(".")
    if len(contig) == 0:
        if len(chars) == 0 or "#" not in chars:
            return 1
        return 0
    f = contig[0]
    if f > len(chars):
        return 0
    if chars[0] == "#":
        if "." not in chars[:f] and (f == len(chars) or chars[f] != "#"):
            return num_ways(chars[f+1:], contig[1:])
        return 0
    if chars[0] == "?":
        if "." not in chars[:f] and (f == len(chars) or chars[f] != "#"):
            return num_ways(chars[f+1:], contig[1:]) + num_ways(chars[1:], contig)
        return num_ways(chars[1:], contig)

out = 0
out2 = 0
for line in open("input.txt"):
    chars, b = tuple(line.strip().split())
    contig = tuple(int(i) for i in b.split(","))
    out += num_ways(chars, contig)
    out2 += num_ways("?".join(chars for _ in range(5)), contig*5)

print(out)
print(out2)
