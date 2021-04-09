
def constructTree(arr, n):
    tree = [[] for _ in range(n+1)]
    for v in arr:
        tree[v[0]].append(v[1])
        tree[v[1]].append(v[0])
    return tree


def dfs(tree, src, par, visited, coloros, c):
    visited[src] = True
    for child in tree[src]:
        if child == par or visited[child] or colors[child-1] != c:
            continue
        dfs(tree, child, src, visited, colors, c)


def Solution(arr, coloros, n):
    blackColoredComponent = 0
    whiteColoredComponent = 0
    tree = constructTree(arr, n)
    print(colors)
    print(tree)
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i] and coloros[i-1] == 0:
            whiteColoredComponent += 1
            dfs(tree, i, 0, visited, coloros, 0)

    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i] and coloros[i-1] == 1:
            blackColoredComponent += 1
            dfs(tree, i, 0, visited, coloros, 1)
    return min(blackColoredComponent, whiteColoredComponent)


N = int(input())
colors = list(map(int, input().split()))
arr = []
for _ in range(N-1):
    v = list(map(int, input().split()))
    arr.append(v)
print(Solution(arr, colors, N))
