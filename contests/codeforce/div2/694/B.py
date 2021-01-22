import math


def Solution(arr, n, x):
    r = []
    for v in arr:
        tmp = v
        count = 0
        while tmp % x == 0:
            count += 1
            tmp = tmp//x
        r.append(count)
    minIdx = 0
    minV = r[0]
    for i in range(1, len(r)):
        if r[i] < minV:
            minV = r[i]
            minIdx = i
    res = sum(arr)
    for _ in range(minV):
        res += sum(arr)
    for u in range(minIdx):
        res += arr[u]

    return res


# op = []
for t in range(int(input())):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N, X))
    print(Solution(arr, N, X))
# print(op)
