import math


def Solution(n, x):
    if n == x:
        return 0

    res = 1
    s = abs(n-x)
    if s < 10:
        return 1
    if s % 10 == 0:
        return s//10
    res += s//10
    return res


# op = []
for t in range(int(input())):
    N, X = map(int, input().split())
    # arr = list(map(int, input().split()))
    # op.append(Solution(N, X))
    print(Solution(N, X))
# print(op)
