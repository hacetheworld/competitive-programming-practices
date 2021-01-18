import math


def Solution(l1, l2, l3, n1, n2, n3):
    # Solution
    hm = {}
    hm[0] = l1
    hm[1] = l2
    hm[2] = l3
    firstSmallSet = 0
    firstSmallEl = min(l1)
    secondSmallSet = 1
    secondSmallEl = min(l2)
    for i in range(3):
        if i != firstSmallSet and firstSmallEl > min(hm[i]):
            firstSmallSet = i
            firstSmallEl = min(hm[i])
        if i != firstSmallSet and i != secondSmallSet and secondSmallEl > min(hm[i]):
            secondSmallSet = i
            secondSmallEl = min(hm[i])
    s1 = 0
    for i in range(3):
        if i != firstSmallSet:
            s1 += sum(hm[i])
    s1 = s1-secondSmallEl
    s2 = sum(hm[firstSmallSet])-firstSmallEl
    s3 = secondSmallEl-s2
    s4 = s1-firstSmallEl
    # print(s1, s2, s3, s4)
    res = abs(s3)+abs(s4)
    return res


# op = []
# for t in range(int(input())):
N1, N2, N3 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
# op.append(Solution(l1,l2,l3,N1,N2,N3))
print(Solution(l1, l2, l3, N1, N2, N3))
# print(op)
