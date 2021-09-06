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


def dfs(adjList, n, src, c, color):
    if src in color:
        return 0
    color[src] = c
    tmp = 1 if src <= n else 0
    for child in adjList[src]:
        tmp += dfs(adjList, n, child, c, color)
    return tmp


def Solution(a, n, m):
    # Write Your Code Here
    adjList = [[] for _ in range(n+1)]
    for i in range(m):
        itm = a[i]
        if itm[0]:
            if len(itm) > 2:
                for j in range(1, len(itm)-1):
                    u = itm[j]
                    v = itm[j+1]
                    adjList[u].append(v)
                    adjList[v].append(u)
            else:
                adjList[itm[1]].append(itm[1])
    color = {}
    sz = {}
    c = 0
    for i in range(1, n+1):
        if not i in color:
            c += 1
            sz[c] = dfs(adjList, n, i, c, color)
        print(sz[color[i]], end=" ")
    print()


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    a = get_list_of_list(m)
    Solution(a, n, m)


# calling main Function
if __name__ == '__main__':
    main()
