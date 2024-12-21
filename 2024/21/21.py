grid = [["7","8","9"],["4","5","6"],["1","2","3"],["_","0","A"]]
coords = {c: (i,j) for i,l in enumerate(grid) for j,c in enumerate(l)}
def paths_between_nums(num1, num2):
    c1 = coords[num1]
    c2 = coords[num2]
    vertical = ""
    if c1[0]>c2[0]:
        vertical = "^"*(c1[0]-c2[0])
    elif c1[0]<c2[0]:
        vertical = "v"*(c2[0]-c1[0])
    horizontal = ""
    if c1[1]>c2[1]:
        horizontal = "<"*(c1[1]-c2[1])
    elif c1[1]<c2[1]:
        horizontal = ">"*(c2[1]-c1[1])
    if c1[0]==3 and c2[1]==0:
        return [vertical+horizontal]
    if c1[1]==0 and c2[0]==3:
        return [horizontal+vertical]
    return list(set([vertical+horizontal, horizontal+vertical]))
    
def num_to_dir(s):
    possible_out = [p+"A" for p in paths_between_nums("A", s[0])]
    for i in range(len(s)-1):
        n = []
        p = paths_between_nums(s[i], s[i+1])
        for prev in possible_out:
            for path in p:
                n.append(prev+path+"A")
        possible_out = n
    return possible_out

grid_dir = [["_","^","A"],["<","v",">"]]
coords_dir = {c: (i,j) for i,l in enumerate(grid_dir) for j,c in enumerate(l)}

def paths_between_dirs(dir1, dir2):
    c1 = coords_dir[dir1]
    c2 = coords_dir[dir2]
    vertical = ""
    if c1[0]>c2[0]:
        vertical = "^"*(c1[0]-c2[0])
    elif c1[0]<c2[0]:
        vertical = "v"*(c2[0]-c1[0])
    horizontal = ""
    if c1[1]>c2[1]:
        horizontal = "<"*(c1[1]-c2[1])
    elif c1[1]<c2[1]:
        horizontal = ">"*(c2[1]-c1[1])
    if c1[0]==0 and c2[1]==0:
        return [vertical+horizontal]
    if c1[1]==0 and c2[0]==0:
        return [horizontal+vertical]
    return list(set([vertical+horizontal, horizontal+vertical]))

def dir_to_dir(s):
    possible_out = [p+"A" for p in paths_between_dirs("A", s[0])]
    for i in range(len(s)-1):
        n = []
        p = paths_between_dirs(s[i], s[i+1])
        for prev in possible_out:
            for path in p:
                n.append(prev+path+"A")
        possible_out = n
    return possible_out

out = 0
for line in open("input.txt").read().splitlines():
    dir1 = num_to_dir(line)
    dir2 = []
    for d in dir1:
        dir2.extend(dir_to_dir(d))
    dir3 = []
    for d in dir2:
        dir3.extend(dir_to_dir(d))
    out += int(line[:3]) * min(len(d) for d in dir3)
print(out)
