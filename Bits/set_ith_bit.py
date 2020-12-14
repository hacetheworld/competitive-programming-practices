def setIthBit(N, i):
    N = N | (1 << i)
    return N


N, i = map(int, input().split())
print(setIthBit(N, i))
