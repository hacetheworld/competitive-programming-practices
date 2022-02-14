def maxSubarray(arr, n):
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        if dp[i-1]+arr[i] > 0:
            dp[i] = arr[i]+dp[i-1]
        else:
            dp[i] = 0

    print(dp)


n = int(input())
arr = [int(c) for c in input().split()]
maxSubarray(arr, n)
