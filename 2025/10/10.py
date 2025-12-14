import re
import itertools
import functools

@functools.cache
def possibilities(lights_bits, wiring_bits):
    out = []
    if lights_bits == 0:
        out.append([])
    for num_buttons_selected in range(1, len(wiring_bits)+1):
        for comb in itertools.combinations(enumerate(wiring_bits), num_buttons_selected):
            if functools.reduce(lambda x,y: x^y, (c for i,c in comb)) == lights_bits:
                out.append([i for i,c in comb])
    return out

# based on https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/
@functools.cache
def part2(wiring_nums, joltage_nums):
    if all(j==0 for j in joltage_nums):
        return [tuple(0 for _ in wiring_nums)]
    ...
    out = set()
    joltage_parity = [i%2 for i in joltage_nums]
    joltage_parity_bits = sum(j*2**i for i,j in enumerate(joltage_parity))
    wiring_bits = tuple(sum(2**i for i in w) for w in wiring_nums)
    poss = possibilities(joltage_parity_bits, wiring_bits)
    for p in poss:
        new_joltage_nums = [j for j in joltage_nums]
        for wiring_num in p:
            for w in wiring_nums[wiring_num]:
                new_joltage_nums[w] -= 1
        ...
        if any(j < 0 for j in new_joltage_nums):
            continue
        ...
        for child in part2(wiring_nums, tuple(j//2 for j in new_joltage_nums)):
            out.add(tuple(2*child[i] + (i in p) for i in range(len(child))))
    return out

def main():
    out = 0
    out2 = 0
    for line in open("input.txt").read().splitlines():
        lights, wiring, joltage = re.match(r"\[([.#]+)\] ([\d, ()]+) \{(.+)\}", line).groups()
        lights_bits = sum((c=="#")*2**i for i,c in enumerate(lights))
        wiring_nums = tuple(tuple(map(int,w[1:-1].split(","))) for w in wiring.split())
        wiring_bits = tuple(sum(2**i for i in w) for w in wiring_nums)
        joltage_nums = tuple(int(j) for j in joltage.split(","))

        
        out += min((len(p) for p in possibilities(lights_bits, wiring_bits)), default=0)

        p2 = part2(wiring_nums, joltage_nums)
        out2 += min(sum(p) for p in p2)
        
    print(out)
    print(out2)

main()
