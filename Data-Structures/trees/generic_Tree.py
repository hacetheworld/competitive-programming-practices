class GenericTree():
    def __init__(self, size):
        self.adjList = [[] for _ in range(size+1)]

    def createTree(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def dfs(self, curr, par):
        print(curr, par)
        for neighbor in self.adjList[curr]:
            if neighbor == par:
                continue
            self.dfs(neighbor, curr)


N = int(input())
Gt = GenericTree(N)

for t in range(N-1):
    u, v = map(int, input().split())
    Gt.createTree(u, v)
print(Gt.adjList)
Gt.dfs(1, -1)
