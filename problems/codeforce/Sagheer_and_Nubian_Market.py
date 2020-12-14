def Solution(arr, N, S):
    # Solution
    l = 0
    r = N
    ans = [0, 0]
    while l <= r:
        mid = (l+r)//2
        res = isValid(arr, S, mid)
        if res[0]:
            l = mid+1
            ans = (mid, res[1])
        else:
            r = mid-1
    return ans


def isValid(arr, S, k):
    tempArr = []
    for j in range(len(arr)):
        tempArr.append(arr[j] + (j + 1) * k)
    tempArr = sorted(tempArr)
    tempSum = 0
    for i in range(k):
        tempSum += tempArr[i]
        if tempSum > S:
            return [False, 0]
    return [True, tempSum]


N, S = map(int, input().split())
arr = list(map(int, input().split()))
res = Solution(arr, N, S)
print(res[0], res[1])
