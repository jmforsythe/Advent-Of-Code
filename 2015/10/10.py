def look_and_say(seq):
    out = []
    ptr = 1
    cur = seq[0]
    count = 1
    n = len(seq)
    while ptr < n:
        if seq[ptr] == cur:
            count += 1
        else:
            out.extend([count, cur])
            cur = seq[ptr]
            count = 1
        ptr += 1
    out.extend([count, cur])
    return out

def do_func_n_times(func, n, initial_input):
    cur = initial_input
    for i in range(n):
        cur = func(cur)
    return cur

ans_40 = do_func_n_times(look_and_say, 40, [int(c) for c in open("input.txt").read().rstrip()])
print(len(ans_40))
ans_50 = do_func_n_times(look_and_say, 10, ans_40)
print(len(ans_50))
