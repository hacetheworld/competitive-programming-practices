import sys
sys.setrecursionlimit(1 << 30)


def constructTree(arr, n):
    tree = [[] for _ in range(n+1)]
    for v in arr:
        tree[v[0]].append(v[1])
        tree[v[1]].append(v[0])
    return tree


def Solution(arr, coloros, n):
    tree = constructTree(arr, n)
    count = 0
    for i in range(1, n+1):
        if coloros[i-1] == 0:
            count += 1
            dfs(tree, i, 0, colors)
    return count


def dfs(tree, src, par, coloros):
    coloros[src-1] = 1
    for child in tree[src]:
        if child == par or colors[child-1] == 1:
            continue
        dfs(tree, child, src, coloros)
    coloros[src-1] = 0


N = int(input())
colors = list(map(int, input().split()))
arr = []
for _ in range(N-1):
    v = list(map(int, input().split()))
    arr.append(v)
print(Solution(arr, colors, N))
