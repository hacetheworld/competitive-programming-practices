import math


def isEmpty(arr):
    pass



def Solution(arr, n):
    # Solution
    res = ""
    for c in arr:
        if c == "1":
            if res[-1] == "1":
                res += "1"
            elif res[-1] == "0":
                res += "1"
            elif res[-1] == "2":
                res += "0"
        else:
            if res[-1] == "1":
                res += "0"
            elif res[-1] == "0":
                res += "1"
            elif res[-1] == "2":
                res += "1"
    return res


for t in range(int(input())):
    N = int(input())
    arr = input()
    # strArr = [input() for _ in range(N)]
    print(Solution(arr, n))
