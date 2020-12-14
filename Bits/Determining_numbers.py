def Solution(arr):
    # Solution
    x = arr[0]
    for i in range(1, len(arr)):
        x ^= arr[i]
    lastBit = getLastBit(x)
    res = 0
    for j in range(len(arr)):
        if isSetBit(arr[j], lastBit):
            res = res ^ arr[j]
    firstNum = res ^ x
    secondNum = res
    if firstNum > secondNum:
        print(secondNum, firstNum)
    else:
        print(firstNum, secondNum)


def isSetBit(v, lastBit):
    return True if v & (1 << lastBit) else False


def getLastBit(x):
    position = 0
    m = 1
    while (not(x & m)):
        m = m << 1
        position += 1
    return position


N = int(input())
arr = list(map(int, input().split()))
Solution(arr)
