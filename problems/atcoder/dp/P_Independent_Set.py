# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout
sys.setrecursionlimit(10**6)
# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------------- SOLUTION FUNCTION ------------------


def waysToPaint(graph, node, par, c, dp, mod):
    if dp[node][c] != -1:
        return dp[node][c]
    ans = 0
    w0 = 1
    for child in graph[node]:
        if child == par:
            continue
        w0 = ((w0)*(waysToPaint(graph, child, node, 0, dp, mod))) % mod
    ans += w0
    if not c:
        w1 = 1
        for child in graph[node]:
            if child == par:
                continue
            w1 = ((w1)*(waysToPaint(graph, child, node, 1, dp, mod))) % mod
        ans = (ans+w1) % mod
    dp[node][c] = ans
    return ans


def Solution(graph, n):
    # Write Your Code Here
    mod = pow(10, 9)+7
    dp = [[-1, -1] for _ in range(n+1)]
    ans = waysToPaint(graph, 1, -1, 0, dp, mod)
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = get_ints_in_variables()
        graph[u].append(v)
        graph[v].append(u)
    Solution(graph, n)


# calling main Function
if __name__ == '__main__':
    main()
