import re

def inc_chr(c):
    if c == "z":
        return "a"
    return chr(ord(c)+1)

def increment(password):
    last = password[-1]
    inc = inc_chr(last)
    if inc == "a":
        return increment(password[:-1]) + inc
    if inc in ("i", "o", "l"):
        inc = inc_chr(inc)
    return password[:-1] + inc

def check1(password):
    prev2 = password[0]
    prev = password[1]
    for c in password[2:]:
        if ord(c) == ord(prev)+1 and ord(prev) == ord(prev2)+1:
            return True
        prev2 = prev
        prev = c
    return False

def check2(password):
    return not ("i" in password or "o" in password or "l" in password)

def check3(password):
    matches = re.findall(r"(.)\1", password)
    return len(set(matches)) >= 2

cur = open("input.txt").read().rstrip()
while not (check1(cur) and check3(cur)):
    cur = increment(cur)
print(cur)

cur = increment(cur)
while not (check1(cur) and check3(cur)):
    cur = increment(cur)
print(cur)
