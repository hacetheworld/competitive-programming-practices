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

# -------------- SOLUTION FUNCTION ------------------


def createArrayListGraph(G, u, v):
    G[u].append(v)
    G[v].append(u)


def dfs(adj, u, p, cc, cnt){
    ma = -1
    cn = 1
    for v in adj[u]:
    if(v == p):
    continue
    dfs(v, u)
    ma = max(cc[v], ma)
    cn += cc[v]
}


ma = max(ma, (n-cn))
cc[u] = cn
cnt[ma].push_back(u)


def Solution(adj, n):
    # Write Your Code Here
    cc = []
    cnt = []


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        adj = [[] for _ in range(n+1)]
        for _ in range(n):
            x, y = get_ints_in_variables()
            createArrayListGraph(adj, x, y)
    Solution(graph, n)


# calling main Function
if __name__ == '__main__':
    main()
