def func(lines, num_batteries):
    out = 0
    for line in lines:
        s = ""
        cur_index = -1
        for bat_num in range(num_batteries):
            next_chr = max(line[cur_index+1:len(line)-(num_batteries-1)+bat_num])
            s += next_chr
            cur_index = line.find(next_chr, cur_index+1)
        out += int(s)
    return out

lines = open("input.txt").read().splitlines()
print(func(lines, 2))
print(func(lines, 12))
