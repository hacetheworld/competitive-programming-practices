import sys
sys.setrecursionlimit(1 << 30)


class GenericTree():
    def __init__(self, size):
        self.adjList = [[] for _ in range(size+1)]

    def createTree(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def dfs(self, curr, par, subordinates):
        count = 0
        for neighbor in self.adjList[curr]:
            if neighbor == par:
                continue
            count += self.dfs(neighbor, curr, subordinates)
        subordinates[curr] = count
        return 1+count


N = int(input())
Gt = GenericTree(N+1)
arr = list(map(int, input().split()))
subordinates = [0 for _ in range(N+1)]
for i in range(len(arr)):
    Gt.createTree(i+2, arr[i])
Gt.dfs(1, -1, subordinates)
for j in range(1, len(subordinates)):
    print(subordinates[j], end=" ")
