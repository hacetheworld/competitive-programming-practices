def pattern(n):
    if n <= 0:
        return
    print(printPattern(n))
    pattern(n-1)


def printPattern(n):
    if n == 0:
        return " "
    res = "* "+printPattern(n-1)
    return res


pattern(5)
