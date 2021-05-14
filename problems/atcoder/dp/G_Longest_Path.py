# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout
sys.setrecursionlimit(10**5)
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


def findlLongestPath(graph, dp, src):
    if dp[src] != -1:
        return dp[src]
    flag = True
    for child in graph[src]:
        flag = False
        dp[src] = max(dp[src], findlLongestPath(graph, dp, child))
    if flag:
        dp[src] = 0
    else:
        dp[src] += 1
    return dp[src]


def Solution(graph, n, m):
    # Write Your Code Here
    dp = [-1 for _ in range(n+2)]
    ans = 0
    for src in range(1, n+1):
        ans = max(ans, findlLongestPath(graph, dp, src))
    print(ans)


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    graph = [[] for _ in range(n+2)]
    for _ in range(m):
        u, v = get_ints_in_variables()
        graph[u].append(v)
    Solution(graph, n, m)


# calling main Function
if __name__ == '__main__':
    main()
