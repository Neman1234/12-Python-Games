import random
from collections import deque

WIDTH, HEIGHT = 10, 10

# start with all open paths
maze = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# randomly add walls
for i in range(HEIGHT):
    for j in range(WIDTH):
        if random.random() < 0.3:   # 30% chance wall
            maze[i][j] = 1

start = (0, 0)
end = (HEIGHT - 1, WIDTH - 1)

maze[start[0]][start[1]] = 0
maze[end[0]][end[1]] = 0

# BFS solver
def bfs(start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            break

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

    # rebuild path
    path = []
    node = end

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path

path = bfs(start, end)

# print maze
for i in range(HEIGHT):
    for j in range(WIDTH):
        if (i, j) in path:
            print("P", end=" ")
        elif maze[i][j] == 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()