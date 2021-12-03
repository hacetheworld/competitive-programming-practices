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


def doDfs(arr, n, m, i, j, pos, s, vis):
    if i >= n or i < 0 or j >= m or j < 0:
        return 0
    if arr[i][j] != s[pos % 4]:
        return 0
    if arr[i][j] == "A" and vis[i][j] == True:
        return float("inf")
    tmp = 0
    extr = 0
    if s[pos % 4] == "A":
        extr += 1
    vis[i][j] = True
    irw = [0, 1, 0, -1]
    jcol = [1, 0, -1, 0]
    for k in range(4):
        tmp = max(tmp, doDfs(arr, n, m, i +
                             irw[k], j+jcol[k], pos+1, s, vis))
        if tmp == float("inf"):
            return float("inf")
    vis[i][j] = False
    return tmp+extr


def Solution():
    # Write Your Code Here
    # n, m = get_ints_in_variables()
    # arr = [[c for c in get_string()] for _ in range(n)]
    # ans = 0
    # s = "DIMA"
    n, m = map(int, input().split())
    m += 1
    q = {'I': 0, 'M': 1, 'A': 2, 'D': 3}
    t = []
    for i in range(n):
        t += map(q.get, input())
        t.append(-7)
    t += [-7] * m
    print(t)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
