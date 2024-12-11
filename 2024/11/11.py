from functools import cache

stones = list(map(int, open("input.txt").read().strip().split()))

@cache
def length_after_iter(num, iter):
    if iter == 0:
        return 1
    if num == 0:
        return length_after_iter(1, iter-1)
    if len(x:=str(num)) % 2 == 0:
        return length_after_iter(int(x[:len(x)//2]), iter-1) + length_after_iter(int(x[len(x)//2:]), iter-1)
    else:
        return length_after_iter(num*2024, iter-1)

print(sum(length_after_iter(s, 25) for s in stones))
print(sum(length_after_iter(s, 75) for s in stones))
