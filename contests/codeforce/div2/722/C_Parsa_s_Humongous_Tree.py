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


def dfs(tree, src, par, lrs, dp):
    for child in tree[src]:
        if child != par:
            dfs(tree, child, src, lrs, dp)
            dp[src][0] += max((abs(lrs[src][0]-lrs[child][0]))+dp[child]
                              [0], (abs(lrs[src][0]-lrs[child][1]))+dp[child][1])
            dp[src][1] += max((abs(lrs[src][1]-lrs[child][0]))+dp[child]
                              [0], (abs(lrs[src][1]-lrs[child][1]))+dp[child][1])


def Solution(tree, lrs, n):
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        lrs = [[0, 0]]
        for _ in range(n):
            x, y = get_ints_in_variables()
            lrs.append([x, y])
        Tree = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = get_ints_in_variables()
            Tree[u].append(v)
            Tree[v].append(u)
        dp = [[0, 0] for _ in range(n+1)]
        dfs(Tree, 1, -1, lrs, dp)
        print(max(dp[1]))


# calling main Function
if __name__ == '__main__':
    main()
