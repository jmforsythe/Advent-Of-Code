grid = [[int(c) for c in line.strip()] for line in open("input.txt")]

DIRS = ((1,0),(0,1),(-1,0),(0,-1))

from heapq import heappop, heappush

def dijkstra(par1, par2):
    distances = dict()
    visited = set()
    q = [(0,0,0,None)]
    while q:
        dist, i, j, dir = heappop(q)
        if (i, j, dir) in visited:
            continue
        visited.add((i, j, dir))
        for d in DIRS:
            if d == dir or dir == (-d[0], -d[1]):
                continue
            added_cost = 0
            for step in range(1,par2+1):
                new_i = i+d[0]*step
                new_j = j+d[1]*step
                if new_i not in range(len(grid)) or new_j not in range(len(grid[0])):
                    continue
                added_cost += grid[new_i][new_j]
                if step < par1:
                    continue
                combined_cost = dist + added_cost
                if (new_i, new_j, dir) in distances and distances[(new_i, new_j, dir)] < combined_cost:
                    continue
                distances[(new_i, new_j, dir)] = combined_cost
                heappush(q, (combined_cost, new_i, new_j, d))
    return distances

print(min(dist for (i, j, dir), dist in dijkstra(1,3).items() if i == len(grid)-1 and j == len(grid[0])-1))
print(min(dist for (i, j, dir), dist in dijkstra(4,10).items() if i == len(grid)-1 and j == len(grid[0])-1))
