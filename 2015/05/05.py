import re
from collections import Counter

def is_nice(s):
    count = Counter(s)
    vowels = ("a","e","i","o","u")
    vowel_count = sum(count[v] for v in vowels if v in count)
    if vowel_count < 3:
        return False
    double = False
    prev = None
    for c in s:
        if c == prev:
            double = True
        if (prev, c) in (("a","b"), ("c","d"), ("p","q"), ("x","y")):
            return False
        prev = c
    return double

print(sum(is_nice(l) for l in open("input.txt").readlines()))

def is_nice_2(s):
    return bool(re.match(r".*(..).*\1.*", s)) and bool(re.match(r".*(.).\1.*", s))

print(sum(is_nice_2(l) for l in open("input.txt").readlines()))
