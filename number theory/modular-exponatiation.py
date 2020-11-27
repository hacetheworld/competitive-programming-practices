def recurPowerModularFunc(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a
    res = recurPowerModularFunc(((a % c)*(a % c)) % c, b//2, c) % c
    if b & 1:
        return ((a % c)*res) % c
    return res


def iterativeModularFunc(a, b, c):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % c
        a = (a*a) % c
        b = b//2
    return res


a, b = int(input()), int(input())
c = pow(10, 6)+7
# print(c)
print(iterativeModularFunc(a, b, c))
