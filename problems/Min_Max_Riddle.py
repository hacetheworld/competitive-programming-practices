def Solution(arr, N):
    # Solution
    res = []
    res.append(max(arr))
    for r in range(2, N+1):
        minArr = []
        arrOfRange = []
        for i in range(r):
            arrOfRange.append(arr[i])
        minArr.append(min(arrOfRange))
        for j in range(r, len(arr)):
            arrOfRange.pop(0)
            arrOfRange.append(arr[j])
            minArr.append(min(arrOfRange))
        res.append(max(minArr))
    return res


N = int(input())
arr = list(map(int, input().split()))
print(Solution(arr, N))
