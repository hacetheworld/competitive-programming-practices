import sys
sys.setrecursionlimit(1 << 30)


def constructTree(arr, n):
    tree = [[] for _ in range(n+1)]
    for v in arr:
        tree[v[0]].append(v[1])
        tree[v[1]].append(v[0])
    return tree


def countLRDiameter(tree, src, par, diameter):
    leaf = 1
    bestAns = 0
    for child in tree[src]:
        if child == par:
            continue
        leaf = 0
        countLRDiameter(tree, child, src, diameter)
        bestAns = max(bestAns, diameter[child])
    if leaf:
        diameter[src] = 0
    else:
        diameter[src] = 1+bestAns


def countTreeDiameter(tree, src, par, dp, diameter):
    leaf = 1
    childDiameters = []
    bestAns = 0
    for child in tree[src]:
        if child == par:
            continue
        leaf = 0
        countTreeDiameter(tree, child, src, dp, diameter)
        childDiameters.append(diameter[child])
        bestAns = max(bestAns, dp[child])
    numOfChild = len(childDiameters)
    childDiameters = sorted(childDiameters)
    if leaf:
        dp[src] = 0
    elif numOfChild == 1:
        dp[src] = 1+childDiameters[0]
    else:
        dp[src] = 2+childDiameters[numOfChild-1] + childDiameters[numOfChild-2]

    dp[src] = max(dp[src], bestAns)


def Solution(arr, n):
    tree = constructTree(arr, n)
    diameter = [0 for _ in range(n+1)]
    countLRDiameter(tree, 1, -1, diameter)
    dp = [0 for _ in range(n+1)]
    countTreeDiameter(tree, 1, -1, dp, diameter)
    # print(dp)
    return dp[1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N-1)]
print(Solution(arr, N))
