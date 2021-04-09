def constructTree(arr, n):
    tree = [[] for _ in range(n+1)]
    for v in arr:
        tree[v[0]].append(v[1])
        tree[v[1]].append(v[0])
    return tree


def bfs(tree, src, par, step, dp, level):
    level[src] = step
    cnt = 0
    for child in tree[src]:
        if child == par:
            continue
        bfs(tree, child, src, step+1, dp, level)
        cnt += dp[child]
    dp[src] += (1+cnt)


def Solution(arr, n, k):
    tree = constructTree(arr, n)
    dp = [0 for _ in range(n+1)]
    level = [0 for _ in range(n+1)]
    res = 0
    dist = []
    bfs(tree, 1, -1, 0, dp, level)
    for i in range(1, n+1):
        dist.append(level[i]-(dp[i]-1))
    dist = sorted(dist, reverse=True)
    for i in range(k):
        res += dist[i]
    return res


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N-1)]
print(Solution(arr, N, K))
