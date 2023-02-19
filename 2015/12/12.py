import json

def count_num(d, part):
    if isinstance(d, list):
        return sum(count_num(e, part) for e in d)
    if isinstance(d, dict):
        if part == 2 and "red" in d.values():
            return 0
        return sum(count_num(e, part) for e in d.values())
    if isinstance(d, int):
        return d
    return 0

j = json.load(open("input.txt"))
print(count_num(j, 1))
print(count_num(j, 2))
