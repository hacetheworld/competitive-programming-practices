def clearIthBit(N, i):
    N = N & (~(1 << i))
    return N


N, i = map(int, input().split())
print(clearIthBit(N, i))
