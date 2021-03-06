import math
# time complexity is log(max(a,b))


def _gcd(a, b):
    if a < b:
        return _gcd(b, a)
    if b == 0:
        return a
    return _gcd(b, a % b)
# a, b = int(input()), int(input())
# print(gcd(a, b))
# extend eculid algo
# for Ax+By=gcd(A,B)


def _extendedGcd(a, b):
    if a < b:
        return _extendedGcd(b, a)
    if b == 0:
        return [a, 1, 0]
    res = _extendedGcd(b, a % b)
    x = res[2]
    y = res[1]-(math.floor(a/b)*res[2])
    res[1] = x
    res[2] = y
    return res


def _lcm(a, b):
    return ((a*b)//_gcd(a, b))


a, b = map(int, input().split())
res = _lcm(a, b)

print(res)
