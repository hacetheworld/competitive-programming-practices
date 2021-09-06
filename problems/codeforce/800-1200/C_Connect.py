# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------
sys.setrecursionlimit(100000)


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


def dfs(grid, n, i, j, visited):
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if grid[i][j] or visited[i][j]:
        return
    visited[i][j] = True
    dfs(grid, n, i-1, j, visited)
    dfs(grid, n, i+1, j, visited)
    dfs(grid, n, i, j+1, visited)
    dfs(grid, n, i, j-1, visited)


def getLastPoint(visited):
    pnt = []
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j]:
                pnt.append([i+1, j+1])
    return pnt


def Solution(grid, n, s, e):
    # Write Your Code Here
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dfs(grid, n, s[0]-1, s[1]-1, visited)
    ps = getLastPoint(visited)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dfs(grid, n, e[0]-1, e[1]-1, visited)
    pl = getLastPoint(visited)
    ans = float("inf")
    for i in range(len(ps)):
        for j in range(len(pl)):
            a = ps[i][0]-pl[j][0]
            b = ps[i][1]-pl[j][1]
            tmp = (a*a)+(b*b)
            ans = min(ans, tmp)
    print(ans if ans != float("inf") else 0)


def main():
    # Take input Here and Call solution function
    n = get_int()
    s = get_ints_in_list()
    e = get_ints_in_list()
    grid = [[int(c) for c in get_string()] for _ in range(n)]
    Solution(grid, n, s, e)


# calling main Function
if __name__ == '__main__':
    main()
