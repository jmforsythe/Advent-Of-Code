import functools
import re

vals = dict()

for l in open("input.txt").readlines():
    lhs, rhs = l.rstrip().split(" -> ")
    vals[rhs] = lhs

@functools.cache
def evaluate(rhs):
    try:
        return int(rhs)
    except:
        pass
    lhs = vals[rhs]
    if len(lhs.split()) == 1:
        return evaluate(lhs)
    if re.match("NOT", lhs):
        return (~evaluate(lhs.split()[1])) % 65536
    p1, op, p2 = lhs.split()
    if op == "AND":
        return (evaluate(p1) & evaluate(p2)) % 65536
    if op == "OR":
        return (evaluate(p1) | evaluate(p2)) % 65536
    if op == "LSHIFT":
        return (evaluate(p1) << evaluate(p2)) % 65536
    if op == "RSHIFT":
        return (evaluate(p1) >> evaluate(p2)) % 65536

a1 = evaluate("a")
evaluate.cache_clear()
vals["b"] = str(a1)
a2 = evaluate("a")
print(a1)
print(a2)
