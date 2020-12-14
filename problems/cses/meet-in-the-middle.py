def makeSum(arr, sum):
    return makeSumHelperFast(arr, sum)


def makeSumHelper(arr, i, sum):
    if sum == 0:
        return 1
    if i == len(arr) or sum < 0:
        return 0
    if i < len(arr):
        if arr[i] <= sum:
            return (makeSumHelper(arr, i+1, sum-arr[i])+makeSumHelper(arr, i+1, sum))
    return makeSumHelper(arr, i+1, sum)


def makeSumHelperFast(arr, sum):
    dp = [[0 for _ in range(sum+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)):
        dp[i][0] = 1

    for j in range(1, len(dp)):
        for k in range(1, len(dp[0])):
            if arr[j-1] <= k:
                dp[j][k] = dp[j-1][k]+dp[j][k-arr[j-1]]
            else:
                dp[j][k] = dp[j-1][k]
    print(dp)
    return dp[-1][-1]


N, S = map(int, input().split())
arr = list(map(int, input().split()))
print(makeSum(arr, S))
