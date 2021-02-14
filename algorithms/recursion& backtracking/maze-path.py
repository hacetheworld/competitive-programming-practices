def mazePath(n, m, row, col, path):
    if row > n or col > m:
        return 0
    if row == n and col == m:
        print(path)
        return 1
    return mazePath(n, m, row, col+1, path+"R") + mazePath(n, m, row+1, col, path+"D")


n, m = map(int, input().split())
print(mazePath(n, m, 0, 0, ""))
