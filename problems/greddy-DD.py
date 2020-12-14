def Solution(arr, N, K):
    # Solution
    maxCoin = 0
    runningCoin = 0
    for i in range(K):
        runningCoin += arr[i]
    maxCoin = runningCoin
    for j in range(K, N+K-1):
        idx = j % N
        lastIdx = j-K
        runningCoin += arr[idx]
        runningCoin -= arr[lastIdx]
        if runningCoin > maxCoin:
            maxCoin = runningCoin
    return maxCoin


for t in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(Solution(arr, N, K))
