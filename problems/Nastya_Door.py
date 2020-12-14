def Solution(arr, N, K):
    # Solution
    p = 0
    l = 0
    for i in range(len(arr)-K):
        runningCount = 0
        for j in range(i, i+K-1):
            if isPeak(arr, j):
                runningCount += 1
        if runningCount > p:
            p = runningCount
            l = i

    return (p+1, l+1)


def isPeak(arr, i):
    return i > 0 and i < len(arr) and arr[i] > arr[i-1] and arr[i] > arr[i+1]


for t in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print("Output Is : ", Solution(arr, N, K))
