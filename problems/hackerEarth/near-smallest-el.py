def NeareastGreatestElement(arr):
    stack = []
    res = []

    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    return res


arr = list(map(int, input().split()))
print(NeareastGreatestElement(arr))
