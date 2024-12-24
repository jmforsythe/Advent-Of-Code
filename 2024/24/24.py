values = {}
i = 0
for line in open("input.txt").read().splitlines():
    i += 1
    if line == "":
        break
    key, val = line.split(": ")
    values[key] = bool(int(val))

gates = {}
q = []
import re
for line in open("input.txt").read().splitlines()[i:]:
    a,op,b,out = re.match(r"(.+) (.+) (.+) -> (.+)", line).groups()
    q.append((a,op,b,out))
    gates[out] = f"({a} {op} {b})"

def run(values, q, swap=[]):
    for left,right in swap:
        for i, (a,op,b,out) in enumerate(q):
            if out == left:
                q[i] = (a,op,b,right)
            elif out == right:
                q[i] = (a,op,b,left)
    while q:
        for i in range(len(q)):
            if i>=len(q):
                break
            a,op,b,out = q[i]
            if a in values and b in values:
                q.pop(i)
                i -= 1
                if op == "AND":
                    values[out] = values[a] and values[b]
                elif op == "XOR":
                    values[out] = values[a] != values[b]
                else:
                    values[out] = values[a] or values[b]
    return sum(2**i*values[key] for i,key in enumerate(sorted([key for key in values if key[0] == "z"])))

z = run({**values}, [*q])
print(z)

# manually add these until desired outcome
swaps = []
for left,right in swaps:
    tmp = gates[left]
    gates[left] = gates[right]
    gates[right] = tmp

stack = [key for key in gates if key[0] == "z"]
while stack:
    key = stack.pop()
    left, op, right = gates[key].strip("()").split()
    l = re.search(r"[a-z]{3}", left)
    r = re.search(r"[a-z]{3}", right)
    if (l and re.search(r"[a-z]{3}", gates[l.group(0)])) or (r and re.search(r"[a-z]{3}", gates[r.group(0)])):
        stack.append(key)
        if l and re.search(r"[a-z]{3}", gates[l.group(0)]):
            stack.append(l.group(0))
        if r and re.search(r"[a-z]{3}", gates[r.group(0)]):
            stack.append(r.group(0))
    else:
        a = gates[left] if left[0] not in "xy" else left
        b = gates[right] if right[0] not in "xy" else right
        gates[key] = f"({max(a,b)} {op} {min(a,b)})"

for zi in sorted([gate for gate in gates if gate[0] == "z"]):
    xs = [0 for _ in range(46)]
    ys = [0 for _ in range(46)]
    for m in re.findall(r"[xy]\d{2}", gates[zi]):
        if m[0]=="x":
            xs[int(m[1:])] += 1
        else:
            ys[int(m[1:])] += 1
    # manually inspect the output
    print(zi, "".join(map(str,xs)), "".join(map(str,ys)), gates[zi].count(" OR"), gates[zi].count("XOR"), gates[zi].count("AND"))
    #print(gates[zi])

out = []
for pair in swaps:
    out.extend(pair)
print(",".join(sorted(out)))
