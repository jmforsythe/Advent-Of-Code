import hashlib

t = open("input.txt").read().rstrip()

i = 0
while hashlib.md5((t + str(i)).encode()).hexdigest()[:5] != "00000":
    i += 1
print(i)

i = 0
while hashlib.md5((t + str(i)).encode()).hexdigest()[:6] != "000000":
    i += 1
print(i)
