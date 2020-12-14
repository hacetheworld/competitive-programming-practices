def factor(N):
    factors = []
    i = 1
    while i*i <= N:
        if N % i == 0:
            factors.append(i)
            if i != N//i:
                factors.append(N//i)
        i += 1
    return sorted(factors)


N = int(input())
print(factor(N))
