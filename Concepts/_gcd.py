import math


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)
# a, b = int(input()), int(input())
# print(gcd(a, b))
# extend eculid algo
# for Ax+By=gcd(A,B)


def extendedGcd(a, b):
    if a < b:
        return extendedGcd(b, a)
    if b == 0:
        return [a, 1, 0]
    res = extendedGcd(b, a % b)
    x = res[2]
    y = res[1]-(math.floor(a/b)*res[2])
    res[1] = x
    res[2] = y
    return res


a, b = int(input()), int(input())
res = extendedGcd(a, b)
temp = res[2]
res[2] = res[1]
res[1] = temp
print("Res , X,Y ->", res)
