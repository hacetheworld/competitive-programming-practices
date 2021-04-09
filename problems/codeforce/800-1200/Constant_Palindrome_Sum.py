def Solution(arr, N, K):
    # Solution
    count = float("inf")
    runningCount = 0
    pairs = makePairs(arr)
    rangeOfSum = 2*K
    for x in range(2, rangeOfSum+1):
        runningCount = 0
        for pair in pairs:
            r1 = pair[0]
            r2 = pair[1]
            if r1+r2 == x:
                continue
            if (r1 > x and r2 > x):
                runningCount += 2
            elif (r1 < x and r2 < x):
                if r1+K+r2 < x:
                    runningCount += 2
                else:
                    runningCount += 1
            else:
                runningCount += 1
        count = min(count, runningCount)
    return count


def makePairs(arr):
    pairs = []
    i, j = 0, len(arr)-1
    while i < j:
        pairs.append([arr[i], arr[j]])
        i += 1
        j -= 1
    return pairs


for t in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # strArr = [input() for _ in range(N)]
    print(Solution(arr, N, K))
