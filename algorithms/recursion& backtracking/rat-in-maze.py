def ratInMaze(maze, n, m, row, col, visited):
    if not isValid(n, m, row, col, visited):
        return
    if row == n-1 and col == m-1:
        return 1
    visited[row][col] = True
    total = 0
    if isValid(n, m, row+1, col, visited) and maze[row+1][col] != 1:
        total += ratInMaze(maze, n, m, row+1, col, visited)
    if isValid(n, m, row-1, col, visited) and maze[row-1][col] != 1:
        total += ratInMaze(maze, n, m, row-1, col, visited)
    if isValid(n, m, row, col+1, visited) and maze[row][col+1] != 1:
        total += ratInMaze(maze, n, m, row, col+1, visited)
    if isValid(n, m, row, col-1, visited) and maze[row][col-1] != 1:
        total += ratInMaze(maze, n, m, row, col-1, visited)
    visited[row][col] = False
    return total


def isValid(n, m, row, col, visited):
    if row >= 0 and row < n and col < m and col >= 0 and visited[row][col] == False:
        return True
    else:
        return False


n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
visited = [[False for _ in range(n)] for _ in range(n)]
print(ratInMaze(maze, n, n, 0, 0, visited))
