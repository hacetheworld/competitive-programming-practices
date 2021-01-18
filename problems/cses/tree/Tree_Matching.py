import sys
sys.setrecursionlimit(1 << 30)


def constructTree(arr, n):
    tree = [[] for _ in range(n+1)]
    for v in arr:
        tree[v[0]].append(v[1])
        tree[v[1]].append(v[0])
    return tree


def Solution(arr, n):
    dp = [[0, 0] for _ in range(n+1)]
    dfs(arr, 1, 0, dp)
    return max(dp[1][0], dp[1][1])


def dfs(tree, src, par, dp):
    leaf = 1
    for child in tree[src]:
        if child == par:
            continue
        leaf = 0
        dfs(tree, child, src, dp)
    if leaf:
        return
    prefix = []
    suffix = []
    for child in tree[src]:
        if child == par:
            continue
        prefix.append(max(dp[child][0], dp[child][1]))
        suffix.append(max(dp[child][0], dp[child][1]))

    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]
    for j in range(len(suffix)-2, -1, -1):
        suffix[j] += suffix[j+1]
    dp[src][0] = suffix[0]
    c_no = 0
    for child in tree[src]:
        if child == par:
            continue
        left = 0 if c_no == 0 else prefix[c_no-1]
        right = 0 if (len(suffix)-1 == c_no) else suffix[c_no+1]
        dp[src][1] = max(dp[src][1], (1+left+right+dp[child][0]))
        c_no += 1


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    v = list(map(int, input().split()))
    tree[v[0]].append(v[1])
    tree[v[1]].append(v[0])
print(Solution(tree, N))
