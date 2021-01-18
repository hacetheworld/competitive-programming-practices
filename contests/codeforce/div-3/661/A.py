import math


def Solution(arr, n):
    arr = sorted(arr, reverse=True)
    for i in range(1, len(arr)):
        if abs(arr[i]-arr[i-1]) >= 2:
            return "NO"

    return "YES"


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)
#
