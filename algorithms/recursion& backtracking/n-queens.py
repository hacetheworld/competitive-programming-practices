def ratInMaze(board, n, m, row, queens):
    if queens == 0:
        print("----------One Possible Solution Start Here-------")
        for i in range(n):
            for j in range(m):
                print(board[i][j], end=" ")
            print("")
        print("--------Possible Solution End Here -------")
        return 1
    if not isValid(n, m, row):
        return 0
    count = 0
    for i in range(m):
        board[row][i] = "Q"
        if canPlaceQueen(board, n, m, row, i):
            count += ratInMaze(board, n, m, row+1, queens-1)
        board[row][i] = 0
    return count


def canPlaceQueen(board, n, m, r, c):
    # // Check Up
    for i in range(r-1, -1, -1):
        if board[i][c] == "Q":
            return False
    # // Check Down
    for i in range(r+1, n):
        if board[i][c] == "Q":
            return False
    # // Check left
    for i in range(c-1, -1, -1):
        if board[r][i] == "Q":
            return False
    # // Check right
    for i in range(c+1, m):
        if board[r][i] == "Q":
            return False
    # // Check upper left dignoal
    i = r-1
    j = c-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    # // Check upper right dignoal
    i = r-1
    j = c+1
    while i >= 0 and j < m:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    # // Check down ift dignoal
    i = r+1
    j = c-1
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1
    # // Check down right dignoal
    i = r+1
    j = c+1
    while i < n and j < m:
        if board[i][j] == "Q":
            return False
        i += 1
        j += 1

    return True


def isValid(n, m, row):
    if row >= 0 and row < n:
        return True
    else:
        return False


n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
print(ratInMaze(maze, n, n, 0, 4))
