import math


def findSum(arr, sum):
    l = 0
    r = len(arr)-1
    tmp = arr[l]+arr[r]
    while l < r:
        if tmp == sum:
            return [arr[l], arr[r]]
        elif tmp < sum:
            tmp -= arr[l]
            l += 1
            tmp += arr[l]
        else:
            tmp -= arr[r]
            r -= 1
            tmp += arr[r]
    return -1


def Solution(arr, n):
    # Solution
    temp = []
    res = ["1"]
    if arr[0] == "1":
        temp.append("2")
    else:
        temp.append("1")
    for i in range(1, len(arr)):
        c = arr[i]
        if c == "1":
            if temp[-1] == "1":
                res.append("1")
                temp.append("2")
            elif temp[-1] == "0":
                res.append("1")
                temp.append("2")
            elif temp[-1] == "2":
                res.append("0")
                temp.append("1")
        else:
            if temp[-1] == "1":
                res.append("0")
                temp.append("0")
            elif temp[-1] == "0":
                res.append("1")
                temp.append("1")
            elif temp[-1] == "2":
                res.append("1")
                temp.append("1")
    return "".join(res)


# op = []
for t in range(int(input())):
    N = int(input())
    arr = input()
    # strArr = [input() for _ in range(N)]
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)
