# count Binary Tree
def countBinaryBalancedTree(H, M):
    if H < 0:
        return 0
    if H == 0 or H == 1:
        return 1
    x = countBinaryBalancedTree(H-1, M) % M
    y = countBinaryBalancedTree(H-2, M) % M
    res = (x*x)+2*(x*y)
    return res


count = countBinaryBalancedTree(4, 10000007)
print(count)
