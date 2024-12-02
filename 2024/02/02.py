def part1(seq):
    return all(seq[i+1]-seq[i] in (1,2,3) for i in range(len(seq)-1))

def part2(seq):
    return any(part1(seq[:i]+seq[i+1:]) for i in range(len(seq)))

mat = [[int(j) for j in line.split()] for line in open("input.txt")]
print(sum(part1(l) or part1(l[::-1]) for l in mat))
print(sum(part2(l) or part2(l[::-1]) for l in mat))
