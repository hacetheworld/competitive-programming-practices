def swapping(a, b):
    a = a ^ b
    b = b ^ a
    a = b ^ a
    return (a, b)


a, b = map(int, input().split())
print(swapping(a, b))
