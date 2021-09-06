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


def dfs(graph, src, par, dp, lrs):
    for v in graph[src]:
        if v == par:
            continue
        dfs(graph, v, src, dp, lrs)
        left = lrs[src-1][0]
        l = 0
        r = 0
        right = lrs[src-1][1]
        l += max(dp[v][0]+abs(lrs[v-1][0]-left),
                 dp[v][1]+abs(lrs[v-1][1]-left))
        r += max(dp[v][0]+abs(lrs[v-1][0]-right),
                 dp[v][1]+abs(lrs[v-1][1]-right))
        dp[src][0] += l
        dp[src][1] += r


def Solution(graph, lrsArr, n):
    # Write Your Code Here
    dp = [[0, 0] for _ in range(n+1)]
    dfs(graph, 1, -1, dp, lrsArr)
    # print(dp, "dp")
    print(max(dp[1]))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        lrsArr = get_list_of_list(n)
        graph = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = get_ints_in_variables()
            graph[u].append(v)
            graph[v].append(u)
        Solution(graph, lrsArr, n)


# calling main Function
if __name__ == '__main__':
    main()
