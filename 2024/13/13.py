import re
matches = re.findall(r"Button A: X(.+), Y(.+)\nButton B: X(.+), Y(.+)\nPrize: X=(.+), Y=(.+)", open("input.txt").read())
out = 0
out2 = 0
for m in matches:
    a,c,b,d,x,y = map(int, m)
    x2 = x+10000000000000
    y2 = y+10000000000000
    det = a*d-b*c
    if (det == 0):
        continue
    ap,bp,cp,dp = d,-b,-c,a
    i,j = ap*x+bp*y, cp*x+dp*y
    if not (i % det or j % det):
        i,j = i//det, j//det
        out += 3*i + j
    i,j = ap*x2+bp*y2, cp*x2+dp*y2
    if not (i % det or j % det):
        i,j = i//det, j//det
        out2 += 3*i + j
print(out)
print(out2)
