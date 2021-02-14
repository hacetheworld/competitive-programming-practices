def printWholeNumber(n, op):
    if int(op) > n:
        return
    print(op)
    for i in range(1 if(op == 0) else 0, 10):
        printWholeNumber(n, op*10+i)


printWholeNumber(13, 0)
