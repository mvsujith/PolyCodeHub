from collections import deque

# Directions for Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_boundary(x, y, N, M):
    return x == 0 or x == N-1 or y == 0 or y == M-1

def shortest_path_to_boundary(grid, N, M):
    # Find the starting point (the cell with value 2)
    start = None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                start = (i, j)
                break
        if start:
            break

    # BFS initialization
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = [[False]*m for i in range(n)]
    visited[start[0]][start[1]] = True

    # BFS loop
    while queue:
        x, y, dist = queue.popleft()

        # Check if we're at a boundary cell
        if is_boundary(x, y, N, M):
            return dist

        # Explore the neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # If no path is found to the boundary
    return -1

# Input
N, M = map(int, input().split())  # Number of rows and columns
grid = [list(map(int, input().split())) for _ in range(N)]  # Grid input

# Find the shortest path to the boundary
result = shortest_path_to_boundary(grid, N, M)
print(result)
