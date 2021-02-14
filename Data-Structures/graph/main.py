import sys


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def createGraph(G, u, v):
    G[u].append(v)
    G[v].append(u)


n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n):
    item = get_ints_in_list()
    u = item[0]
    v = item[1]
    createGraph(G, u, v)
print(G)
