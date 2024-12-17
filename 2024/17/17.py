A, B, C, program = [int(l.split(": ")[1]) if i<3 else list(map(int, l.split(": ")[1].split(","))) for i,l in enumerate(open("input.txt").read().splitlines()) if l != ""]
B_init = B
C_init = C
out = []

def combo(i):
    if i <= 3:
        return i
    if i == 4:
        return A
    if i == 5:
        return B
    if i == 6:
        return C

def op(ins, b):
    global A,B,C,program
    a = program[ins]
    if a == 0:
        A //= 2**combo(b)
        return ins+2
    if a == 1:
        B ^= b
        return ins+2
    if a == 2:
        B = combo(b) % 8
        return ins+2
    if a == 3:
        return ins+2 if A==0 else b
    if a == 4:
         B ^= C
         return ins+2
    if a == 5:
        out.append(combo(b)%8)
        return ins+2
    if a == 6:
        B = A // 2**combo(b)
        return ins+2
    if a == 7:
        C = A // 2**combo(b)
        return ins+2

def run(i):
    global A,B,C,out
    A,B,C = i,B_init,C_init
    ins = 0
    out = []
    while ins+1 < len(program):
        ins = op(ins, program[ins+1])
    return out

print(",".join(str(i) for i in run(A)))

possible = [0]
for o in program[::-1]:
    possible = [p*8+i for p in possible for i in range(2**3) if run(p*8+i) == program[-len(run(p*8+i)):]]
print(min(possible))

