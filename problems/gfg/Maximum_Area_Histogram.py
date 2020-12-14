def MaximumAreaHistogram(arr):
    stackForRightSmaller = []
    stackForRLeftSmaller = []
    nearestSmallerRight = []
    nearestSmallerLeft = []
    for i in range(len(arr)-1, -1, -1):
        while len(stackForRightSmaller) > 0 and stackForRightSmaller[-1][0] > arr[i]:
            stackForRightSmaller.pop()
        if len(stackForRightSmaller) == 0:
            nearestSmallerRight.append(-1)
        else:
            nearestSmallerRight.append(stackForRightSmaller[-1][1])
        stackForRightSmaller.append([arr[i], i])
    for i in range(len(arr)):
        while len(stackForRLeftSmaller) > 0 and stackForRLeftSmaller[-1][0] > arr[i]:
            stackForRLeftSmaller.pop()
        if len(stackForRLeftSmaller) == 0:
            nearestSmallerLeft.append(-1)
        else:
            nearestSmallerLeft.append(stackForRLeftSmaller[-1][1])
        stackForRLeftSmaller.append([arr[i], i])
    res = []
    nearestSmallerRight = list(reversed(nearestSmallerRight))
    print(nearestSmallerRight, nearestSmallerLeft)
    for j in range(len(nearestSmallerLeft)):
        idxPair = [nearestSmallerRight[j], nearestSmallerLeft[j]]
        res.append(arr[j]*max(1, ((idxPair[0]-idxPair[1])-1)))
    print(res)
    return max(res)


arr = list(map(int, input().split()))
print(MaximumAreaHistogram(arr))
