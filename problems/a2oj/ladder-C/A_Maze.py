# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout
sys.setrecursionlimit(100000)
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


def dfs(grid, i, j, n, m, k, vis):
    if k <= 0 or i >= n or j >= m or i < 0 or j < 0 or vis[i][j]:
        return k
    if grid[i][j] == "#" or grid[i][j] == "X":
        return k
    vis[i][j] = True
    k = dfs(grid, i+1, j, n, m, k, vis)
    k = dfs(grid, i-1, j, n, m, k, vis)
    k = dfs(grid, i, j+1, n, m, k, vis)
    k = dfs(grid, i, j-1, n, m, k, vis)
    if k > 0:
        grid[i][j] = "X"
        return k-1
    return k


def Solution(grid, n, m, k):
    # Write Your Code Here
    vis = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        f = 0
        for j in range(m):
            c = grid[i][j]
            if c == ".":
                dfs(grid, i, j, n, m, k, vis)
                f = 1
            if f:
                break
        if f:
            break
    for itm in grid:
        print("".join(itm))


def main():
    # Take input Here and Call solution function
    n, m, k = get_ints_in_variables()
    grid = [[c for c in get_string()] for _ in range(n)]
    Solution(grid, n, m, k)


# calling main Function
if __name__ == '__main__':
    main()
