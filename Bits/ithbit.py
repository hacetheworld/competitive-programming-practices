def getIthBit(N, i):
    return 1 if N & (1 << i) else 0


N, i = map(int, input().split())
print(getIthBit(N, i))
