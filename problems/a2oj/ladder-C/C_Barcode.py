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


def helper(arr, m, n, to, x, y, dot, hs):
    ans = float("inf")
    k = 0 if to == "." else 1
    print(k, "k")
    for i in range(m):
        tmp = 0
        cnt = y
        cx = 0
        for j in range(i, m):
            if cnt == 0:
                break
            tmp += arr[j][k]
            cnt -= 1
            cx += 1
            if cx >= x:
                if to == ".":
                    leftHs = ((cx)*n)-tmp
                    totalHs = hs-leftHs
                    ans = min(ans, totalHs+tmp)
                    # print(ans, "ans")
                else:
                    leftdot = ((cx)*n)-tmp
                    totaldot = dot-leftdot
                    ans = min(ans, totaldot+tmp)
                    print(k, "k", "ans", ans, "totaldot", totaldot,
                          "leftdot", leftdot, "tmp", tmp, "cx", cx, "dot", dot, "j", j)
    return ans


def Solution(grid, n, m, x, y):
    # Write Your Code Here
    arr = []
    dot = 0
    hs = 0
    for i in range(m):
        tmp = 0
        for j in range(n):
            if grid[j][i] == ".":
                tmp += 1
        dot += tmp
        hs += (n-tmp)
        arr.append([tmp, n-tmp])
    print(arr)
    ans = helper(arr, len(arr), n, ".", x, y, dot, hs)
    ans = min(ans, helper(arr, len(arr), n, "#", x, y, dot, hs))
    print(ans)


def main():
    # Take input Here and Call solution function
    n, m, x, y = get_ints_in_variables()
    grid = [get_string() for _ in range(n)]
    Solution(grid, n, m, x, y)


# calling main Function
if __name__ == '__main__':
    main()
