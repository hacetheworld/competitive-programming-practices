def kadaineAlg(arr, n):
    ans = -999999999999
    mx = 0
    for i in range(n):
        mx = arr[i]+mx
        if mx < 0:
            mx = 0
        elif mx > ans:
            ans = mx
    if ans == -999999999999:
        return max(arr)
    return ans


def kadaineAlgDp(arr, n):
    dp = [0 for _ in range(n)]
    dp[0] = arr[0] if arr[0] > 0 else 0
    for i in range(1, n):
        if dp[i-1]+arr[i] > 0:
            dp[i] = arr[i]+dp[i-1]
        else:
            dp[i] = 0
    if max(dp) == 0:
        return [max(arr), arr.index(max(arr)), arr.index(max(arr))]
    idj = dp.index(max(dp))
    idi = 0
    for i in range(idj, -1, -1):
        if dp[i] == 0:
            idi = i+1
            break
    # print(dp)
    return [max(dp), idi, idj]
    # print(dp)


def maxRectangle(grid, n, m):
    dp = [0 for _ in range(m)]
    ans = -float("inf")
    cord = []
    for i in range(n):
        dp = [c for c in grid[i]]
        for k in range(i+1, n):
            for j in range(m):
                dp[j] += grid[k][j]
            res = kadaineAlgDp(dp, m)
            if ans < res[0]:
                ans = res[0]
                cord = [i, k, res[1], res[2]]
    print(ans)
    print(cord)


ROW = 4
COL = 5
M = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
maxRectangle(M, ROW, COL)
