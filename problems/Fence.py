def Solution(arr, K):
    # Solution
    minSum = 0
    runningSum = 0
    for i in range(K):
        v = arr[i]
        runningSum += v
    id = 0
    minSum = runningSum
    for j in range(K, len(arr)):
        runningSum = runningSum-arr[j-K]+arr[j]
        if runningSum < minSum:
            id = j-K+1
            minSum = runningSum
    return id+1


N, K = map(int, input().split())
arr = list(map(int, input().split()))
# strArr = [input() for _ in range(N)]
print(Solution(arr, K))
