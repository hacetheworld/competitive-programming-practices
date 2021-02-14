import math


def Solution(arr, n):
    hm = [0 for _ in range(n)]
    total = 0
    for i in range(1, len(arr)-1):
        if is_hv(arr, i):
            total += 1
            hm[i] = 1
    ans = total
    for i in range(1, len(arr)-1):
        temp = arr[i]
        arr[i] = arr[i - 1]
        ans = min(ans, (total - hm[i - 1] - hm[i] - hm[i + 1] +
                        is_hv(arr, i - 1) + is_hv(arr, i) + is_hv(arr, i + 1)))
        arr[i] = arr[i + 1]
        ans = min(ans, (total - hm[i - 1] - hm[i] - hm[i + 1] +
                        is_hv(arr, i - 1) + is_hv(arr, i) + is_hv(arr, i + 1)))
        arr[i] = temp
    return ans


def is_hv(a, j):
    n = len(a)
    return 1 if 0 < j < n - 1 and ((a[j] < a[j-1] and a[j] < a[j+1]) or (a[j] > a[j-1] and a[j] > a[j+1])) else 0


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)
