import math


def Solution(a, b, n):
    s1 = 0
    s1m = min(a)
    for v in a:
        s1 += abs(v-s1m)
    s2 = 0
    s2m = min(b)
    for v in b:
        s2 += abs(v-s2m)
    s3 = 0
    for i in range(n):
        s3 += (min(a[i]-s1m, b[i]-s2m))
    return s1+s2-s3


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))
    # op.append(Solution(arr, ar2, N))
    print(Solution(arr, ar2, N))
# print(op)
#
