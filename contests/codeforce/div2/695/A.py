import math


def Solution(n):
    if n == 1:
        print("9")
        return
    elif n == 2:
        print("98")
        return
    print("989", end="")
    for i in range(3, n):
        print(str((i-3) % 10), end="")
    print("")


for t in range(int(input())):
    N = int(input())
    # arr = list(map(int, input().split()))
    # strArr = [input() for _ in range(N)]
    Solution(N)
