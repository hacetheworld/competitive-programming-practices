def Solution(x):
    if x < 10:
        return x
    if x > 45:
        return -1
    maxNum = 9
    res = []
    while x > 0:
        if x > maxNum:
            res.insert(0, maxNum)
            x -= maxNum
            maxNum = maxNum-1
        else:
            res.insert(0, x)
            x -= x
    num = ""
    for v in res:
        num += str(v)
    return int(num)


for t in range(int(input())):
    X = int(input())
    print(Solution(X))
