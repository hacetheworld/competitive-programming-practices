def Solution(arr, n, m):
    # Solution
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(m):
            if S[0] == arr[i][j]:
                bfs(arr, i, j, S, 0, dp)
    res = -1
    for i in dp:
        temp = max(i)
        if temp > res:
            res = temp
    return res


def bfs(arr, i, j, S, sIdx, dp):
    if isValid(arr, i, j, S, sIdx):
        dp[i][j] = 1
        dx = [0, 0, -1, 1, -1, 1, -1, 1]
        dy = [-1, 1, 0, 0, -1, 1, 1, -1]
        for k in range(8):
            dp[i][j] = max(dp[i][j], bfs(arr, i+dx[k], j+dy[k], S, sIdx+1, dp))
        return 1+dp[i][j]
    else:
        return 0


def isValid(arr, i, j, S, sidx):
    if (i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or sidx > len(S)):
        return False
    else:
        if S[sidx] == arr[i][j]:
            return True
        else:
            return False


for t in range(int(input())):
    H, W = map(int, input().split())
    matrix = [[c for c in input()] for _ in range(H)]
    print("Case {}: {}".format(t+1, Solution(matrix, H, W)))
