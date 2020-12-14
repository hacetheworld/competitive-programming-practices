def bitsRequired(a, b):
    return countBitsFast(a ^ b)


def countBits(N):
    count = 0
    while N > 0:
        count += (N & 1)
        N = N >> 1
    return count


def countBitsFast(N):
    count = 0
    while N:
        count += 1
        N = (N) & (N-1)
    return count


a, b = map(int, input().split())
print(bitsRequired(a, b))
