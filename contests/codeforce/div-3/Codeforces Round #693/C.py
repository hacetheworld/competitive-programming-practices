def Solution(arr, n):
    mx = 0
    dp = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        total = 0
        total += arr[i]
        if (i+arr[i]) < n:
            total += dp[i+arr[i]]
        dp[i] = total
        mx = max(mx, dp[i])
    return mx


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)
