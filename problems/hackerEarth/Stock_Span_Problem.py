def StockSpanProblem(arr):
    stack = []
    nearestGreaterLeft = []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1][0] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            nearestGreaterLeft.append(-1)
        else:
            nearestGreaterLeft.append(stack[-1][1])
        stack.append([arr[i], i])
    res = []
    for j in range(len(nearestGreaterLeft)):
        res.append(max(1, (j-nearestGreaterLeft[j])))
    return res


arr = list(map(int, input().split()))
print(StockSpanProblem(arr))
