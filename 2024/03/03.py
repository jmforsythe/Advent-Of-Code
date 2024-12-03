import re
s = open("input.txt").read()
m = re.compile(r"mul\((\d+),(\d+)\)")
print(sum(int(a)*int(b) for a,b in m.findall(s)))

out = 0
start = 0
while start != -1:
    dont = s.find("don't()", start)
    for a,b in m.findall(s, start, dont):
        out += int(a)*int(b)
    start = s.find("do()", dont)
print(out)
