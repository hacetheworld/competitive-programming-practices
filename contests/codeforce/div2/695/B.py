import math


def Solution(arr, n):
    hm = [0 for _ in range(n+1)]
    ans = 0
    for i in range(1, len(arr)-1):
        if isHill(arr, i) or isValley(arr, i):
            ans += 1
            hm[i] = 1
    total = ans
    for i in range(1, len(arr)-1):
        temp = arr[i]
        arr[i] = arr[i - 1]
        ans = min(ans, total - hm[i - 1] - hm[i] - hm[i + 1] + isHill(arr, i - 1) + isValley(
            arr, i - 1) + isHill(arr, i) + isValley(arr, i) + isHill(arr, i + 1) + isValley(arr, i + 1))
        arr[i] = arr[i + 1]
        ans = min(ans, total - hm[i - 1] - hm[i] - hm[i + 1] + isHill(arr, i - 1) + isValley(
            arr, i - 1) + isHill(arr, i) + isValley(arr, i) + isHill(arr, i + 1) + isValley(arr, i + 1))
        arr[i] = temp

    return ans


def isValley(arr, i):
    if i <= 0 or i >= len(arr)-1:
        return False
    prev = arr[i-1]
    nxt = arr[i+1]
    current = arr[i]
    return (current < prev and current < nxt)


def isHill(arr, i):
    if i <= 0 or i >= len(arr)-1:
        return False
    prev = arr[i-1]
    nxt = arr[i+1]
    current = arr[i]
    return (current > prev and current > nxt)


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)
