lines = [line.strip() for line in open("input.txt")]

dir_map = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}

graph = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            continue
        graph[(i,j)] = set()
        if c == ".":
            for a, b in ((1,0),(0,1),(-1,0),(0,-1)):
                if i+a in range(len(lines)) and j+b in range(len(lines[i+a])):
                    if lines[i+a][j+b] != "#":
                        graph[(i,j)].add((i+a,j+b))
        if c in dir_map:
            a, b = dir_map[c]
            if i+a in range(len(lines)) and j+b in range(len(lines[i+a])):
                if lines[i+a][j+b] != "#":
                    graph[(i,j)].add((i+a,j+b))

start = next((0,j) for j, c in enumerate(lines[0]) if c == ".")

def find_longest(pos, seen):
    count = 0
    while pos[0] != len(lines)-1:
        connections = graph[pos] - seen
        count += 1
        seen.add(pos)
        if len(connections) == 0:
            return (-1,seen)
        if len(connections) > 1:
            m, s = max((find_longest(c, {s for s in seen}) for c in connections), key=lambda x:x[0])
            return (count + m, seen.union(s))
        pos = connections.pop()
    seen.add(pos)
    return count, seen

def print_board(seen):
    for i, line in enumerate(lines):
        r = ""
        for j, c in enumerate(line):
            if (i,j) in s:
                r += "O"
            else:
                r += c
        print(r)

m,s = find_longest(start, set())
print(m)

contracted_graph = {node: {c:1 for c in connections} for node, connections in graph.items()}
for node in contracted_graph:
    for con in contracted_graph[node]:
        contracted_graph[con][node] = 1

q = [pos for pos in contracted_graph if len(contracted_graph[pos]) == 2]
while q:
    for pos in q:
        connections = contracted_graph[pos]
        if len(connections) == 2:
            (p1,w1), (p2,w2) = connections.items()
            dist = max(contracted_graph[p1].get(p2, 0), contracted_graph[pos][p1] + contracted_graph[pos][p2])
            contracted_graph[p1][p2] = dist
            contracted_graph[p2][p1] = dist
            contracted_graph[p1].pop(pos, 0)
            contracted_graph[p2].pop(pos, 0)
            contracted_graph.pop(pos)
            q.remove(pos)
    q = [pos for pos in contracted_graph if len(contracted_graph[pos]) == 2]

matrix = [[contracted_graph[u].get(v,0) for v in contracted_graph] for u in contracted_graph]

m = -1
seen = 0
stack = [(0, 0)]
while stack:
    i, dist = stack.pop()
    if dist == None:
        if seen & (1<<i):
            seen -= (1<<i)
        continue
    if i == len(matrix)-1:
        m = max(m, dist)
        continue
    if seen & (1<<i):
        continue
    seen |= (1<<i)
    stack.append((i, None))
    for j, weight in enumerate(matrix[i]):
        if weight>0:
            stack.append((j, dist+weight))
print(m)
