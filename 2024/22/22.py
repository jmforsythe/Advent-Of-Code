def f(i):
    i ^= i<<6
    i &= (1<<24)-1
    i ^= i>>5
    i &= (1<<24)-1
    i ^= i<<11
    i &= (1<<24)-1
    return i

buyer_sequences = []

out = 0
for line in open("input.txt").read().splitlines():
    seq = [int(line)]
    for _ in range(2000):
        seq.append(f(seq[-1]))
    out += seq[-1]
    buyer_sequences.append(seq)
print(out)

firsts = []

for b in buyer_sequences:
    first = {}
    for start in range(len(b)-4):
        key = tuple((b[start+i+1]%10)-(b[start+i]%10) for i in range(4))
        if key not in first:
            first[key] = b[start+4]%10
    firsts.append(first)

out = 0
for key in set().union(*firsts):
    out = max(out, sum(first[key] if key in first else 0 for best in firsts))
print(out)
