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


def dfs(graph, n, node, visited, ans):
    if not node in visited:
        ans.append(node)
        visited[node] = True
        for child in graph[node]:
            dfs(graph, n, child, visited, ans)


def Solution(graph, n):
    # Write Your Code Here
    ans = []
    visited = {}
    for key in graph:
        if len(graph[key]) == 1:
            dfs(graph, n, key, visited, ans)
            break

    print(*ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    graph = {}
    for _ in range(n):
        x, y = get_ints_in_variables()
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]
        if y in graph:
            graph[y].append(x)
        else:
            graph[y] = [x]
    # print(graph)
    Solution(graph, n)


# calling main Function
if __name__ == '__main__':
    main()
