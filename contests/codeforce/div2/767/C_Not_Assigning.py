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


# def dfs(graph, parent, visited, edgeWeight, ans):
#     if len(graph[parent]) >= 2:
#     for child in graph[parent]:
#         if visited[child]:
#             continue


def Solution(graph, n):
    # Write Your Code Here
    ans = [-1] * (n - 1)
    if max(len(graph[i]) for i in range(n + 1)) > 2:
        print(-1)
        return
    cur, prev = 1, None
    while len(graph[cur]) != 1:
        cur += 1
    for p in range(n - 1):
        for x, i in graph[cur]:
            if x != prev:
                ans[i] = [2, 3][p % 2]
                cur, prev = x, cur
                break
    print(*ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        graph = [[] for _ in range(n+1)]
        for i in range(n-1):
            u, v = get_ints_in_variables()
            graph[u] += [(v, i)]
            graph[v] += [(u, i)]
        Solution(graph, n)


# calling main Function
if __name__ == '__main__':
    main()
