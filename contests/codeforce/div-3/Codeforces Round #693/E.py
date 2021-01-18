def Solution(arr, n):
    tmp = [v for v in arr]
    arr = sorted(arr, key=lambda x: x[0])
    res = []
    print(arr)
    for i in range(len(tmp)):
        r = binarySearchLowerBound(arr, arr[i][1], len(arr))
        if r == -1:
            res.append(r)
        else:
            res.append(r+1)
    return res


def binarySearchLowerBound(arr, key, upBound):
    left = 0
    right = upBound-1
    res = -1
    while left <= right:
        mid = left+((right-left)//2)
        if arr[mid][1] < key:
            return mid
        else:
            right = mid-1
    return res


op = []
for t in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    op.append(Solution(arr, N))
    # print(Solution(arr, N))
print(op)
