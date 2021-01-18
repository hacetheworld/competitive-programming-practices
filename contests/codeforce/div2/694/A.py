import math


def Solution(arr, n, x):
    s1 = 0
    for v in arr:
        s1 += math.ceil(v/x)
    s2 = math.ceil(sum(arr)/x)
    print(min(s1, s2), max(s1, s2))


# op = []
for t in range(int(input())):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    Solution(arr, N, X)
# print(op)
