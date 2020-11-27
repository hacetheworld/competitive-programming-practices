def Solution(arr):
    maxSum = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            maxSum += arr[i]
            count += 1
    return [maxSum, count]


N = int(input())
arr = list(map(int, input().split()))
res = Solution(arr)
print(res[0])
print(res[1])
