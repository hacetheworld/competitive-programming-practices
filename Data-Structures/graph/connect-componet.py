import sys
import math


def createArrayListGraph(G, u, v):
    G[u].append(v)
    G[v].append(u)


def dfs(adjList, src, visited):
    visited[src] = True
    print(src, "->", end=" ")
    for neighbor in adjList[src]:
        if visited[neighbor]:
            continue
        dfs(adjList, neighbor, visited)


def connectComponent(adjList, n):
    visited = [False for _ in range(n+1)]
    res = 0
    for src in range(1, n+1):
        if visited[src]:
            continue
        dfs(Graph, src, visited)
        print("")

        res += 1
    print(res)


Graph = [[] for _ in range(9)]

createArrayListGraph(Graph, 1, 2)
createArrayListGraph(Graph, 2, 3)
createArrayListGraph(Graph, 3, 1)
createArrayListGraph(Graph, 5, 6)
createArrayListGraph(Graph, 6, 7)
createArrayListGraph(Graph, 7, 8)
connectComponent(Graph, 8)
