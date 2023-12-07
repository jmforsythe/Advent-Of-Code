from collections import Counter
from functools import cmp_to_key

lines = open("input.txt").readlines()

def card_compare(card1, card2):
    ranks = ["j","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    return ranks.index(card1)-ranks.index(card2)

def compare(line1, line2):
    hand1 = line1.split()[0]
    hand2 = line2.split()[0]
    hand1 = sorted(list(hand1), key=cmp_to_key(card_compare), reverse=True)
    hand2 = sorted(list(hand2), key=cmp_to_key(card_compare), reverse=True)
    m1 = Counter(hand1).most_common()
    m2 = Counter(hand2).most_common()
    for i, j in zip(m1, m2):
        if x:=i[1]-j[1]:
            return x
    for i, j in zip(line1.split()[0], line2.split()[0]):
        if x:=card_compare(i[0], j[0]):
            return x
    return 0


lines.sort(key=cmp_to_key(compare))
out = 0
for i, line in enumerate(lines):
    hand, bid = line.strip().split()
    out += (i+1) * int(bid)

print(out)

def compare2(line1, line2):
    line1 = line1.replace("J", "j")
    line2 = line2.replace("J", "j")
    hand1 = line1.split()[0]
    hand2 = line2.split()[0]
    hand1 = "".join(sorted(list(hand1), key=cmp_to_key(card_compare), reverse=True))
    hand2 = "".join(sorted(list(hand2), key=cmp_to_key(card_compare), reverse=True))
    m1 = Counter(hand1.replace("j", "")).most_common()
    m2 = Counter(hand2.replace("j", "")).most_common()
    m1 = Counter(hand1.replace("j", m1[0][0] if len(m1) else "j")).most_common()
    m2 = Counter(hand2.replace("j", m2[0][0] if len(m1) else "j")).most_common()
    for i, j in zip(m1, m2):
        if x:=i[1]+-j[1]:
            return x
    for i, j in zip(line1.split()[0], line2.split()[0]):
        if x:=card_compare(i[0], j[0]):
            return x
    return 0

lines.sort(key=cmp_to_key(compare2))
out = 0
for i, line in enumerate(lines):
    hand, bid = line.strip().split()
    out += (i+1) * int(bid)

print(out)