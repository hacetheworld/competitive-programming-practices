import math


def Solution(arr, n, x):
    s = sum(arr)
    res = s
    count = 0
    flag = True
    while flag:
        for i in range(len(arr)):
            if arr[i] % x == 0:
                arr[i] = (arr[i]//x)
            else:
                flagIdx = i
                flag = False
                break
        if flag:
            count += 1
    res += (s*(count))
    for i in range(flagIdx):
        arr[i] = (arr[i]*x)
    print(arr)
    for v in arr:
        if v % x == 0:
            res += v
        else:
            break
    return res


# op = []
for t in range(int(input())):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N, X))
    print(Solution(arr, N, X))
# print(op)
