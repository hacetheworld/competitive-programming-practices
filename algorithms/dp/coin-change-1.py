def coinChange(arr, n, sm):
    dp = [[1 for _ in range(sm+1)] for _ in range(n+1)]
    arr = sorted(arr)
    # print(dp)
    for i in range(n):
        for j in range(1, sm+1):
            if j-arr[i] >= 0:
                dp[i+1][j] = dp[i-1][j]+dp[i-1][j-arr[i]]
    print(dp)
    print(dp[-1][-1])


n = int(input())
arr = [int(c) for c in input()]
sm = int(input())
coinChange(arr, n, sm)
