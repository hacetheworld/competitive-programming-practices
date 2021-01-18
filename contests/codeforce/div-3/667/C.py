import math


def Solution(n, x):
    res = 1
    s = abs(n-x)
    print(s)
    while s > 10:
        res += 1
        s = s-10
    return res


# op = []
for t in range(int(input())):
    N, X = map(int, input().split())
    # arr = list(map(int, input().split()))
    # op.append(Solution(N, X))
    print(Solution(N, X))
# print(op)
