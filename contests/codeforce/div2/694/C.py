import math


def Solution(a, b, n, m):
    a = sorted(a, reverse=True)
    hm = {}
    j = 0
    res = 0
    for i in range(len(a)):
        frnd = a[i]-1
        if b[frnd] in hm:
            res += b[frnd]
        else:
            res += b[j]
            hm[b[j]] = True
            j += 1
    return res


# op = []
for t in range(int(input())):
    N, M = map(int, input().split())
    friends = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    # op.append(Solution(friends, cost, N, M))
    print(Solution(friends, cost, N, M))
# print(op)
