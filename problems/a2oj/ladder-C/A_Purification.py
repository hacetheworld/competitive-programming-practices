# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def check(arr, n):
    outerF = 1
    for i in range(n):
        f = 1
        for r in range(n):
            if arr[i][r] == ".":
                f = 0
                break
        if f == 0:
            continue
        for j in range(n):
            fl = 1
            for c in range(n):
                if arr[c][j] == ".":
                    fl = 0
                    break
            if fl:
                outerF = 0
                break
        if outerF == 0:
            break
    return outerF


def Solution(arr, n):
    # Write Your Code Here
    ans = n
    f = 1
    ans = []
    if not check(arr, n):
        print(-1)
        return
    f = 0
    for v in arr:
        if "E"*n in "".join(v):
            f = 1
            break
    if f:
        for i in range(n):
            for j in range(n):
                if arr[j][i] == ".":
                    ans.append([j+1, i+1])
                    break
    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == ".":
                    ans.append([i+1, j+1])
                    break

    for i in range(len(ans)):
        print(*ans[i])


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = [[c for c in get_string()] for _ in range(n)]
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
