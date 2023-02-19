print(sum(len(l.rstrip()) - len(bytes(l.rstrip(), "utf-8").decode("unicode_escape")) + 2 for l in open("input.txt").readlines()))
print(len([c for c in open("input.txt").read() if c in ("\\", "\"")]) + 2*len(open("input.txt").readlines()))
