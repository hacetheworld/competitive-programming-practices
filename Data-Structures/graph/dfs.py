import sys
import math


def createArrayListGraph(G, u, v):
    G[u].append(v)
    G[v].append(u)


def dfs(adjList, src, visited):
    visited[src] = True
    print(src, end=" ")
    for neighbor in adjList[src]:
        if visited[neighbor]:
            continue
        dfs(adjList, neighbor, visited)


Graph = [[] for _ in range(5)]

createArrayListGraph(Graph, 1, 2)
createArrayListGraph(Graph, 1, 3)
createArrayListGraph(Graph, 3, 4)
createArrayListGraph(Graph, 2, 4)
visited = [False for _ in range(5)]
print(Graph)
dfs(Graph, 1, visited)
