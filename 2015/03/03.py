def get_visited(path):
    coords = (0,0)
    visited = set()
    visited.add(coords)
    for c in path:
        if c == ">":
            coords = (coords[0]+1, coords[1])
        elif c == "<":
            coords = (coords[0]-1, coords[1])
        elif c == "^":
            coords = (coords[0], coords[1]+1)
        elif c == "v":
            coords = (coords[0], coords[1]-1)
        visited.add(coords)
    return visited

l = open("input.txt").read()
s1 = get_visited(l)
s2 = get_visited([c for i, c in enumerate(l) if i%2]) | get_visited([c for i, c in enumerate(l) if not i%2])
print(len(s1))
print(len(s2))
