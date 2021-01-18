def Solution(arr, n):
    sumOfArr = sum(arr)
    ans = n-1
    i = 1
    while i*i <= sumOfArr:
        if sumOfArr % i == 0:
            a1 = check(arr, i)
            a2 = check(arr, sumOfArr//i)
            if a1 != -1:
                ans = min(a1, ans)
            if a2 != -1:
                ans = min(a2, ans)
        i += 1
    return ans


def check(arr, i):
    count = 0
    tempSum = 0
    k = 0
    for j in range(len(arr)):
        tempSum += arr[j]
        if tempSum == i:
            count += (j-k)
            k = j+1
            tempSum = 0
        if tempSum > i:
            return -1
    return count


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(Solution(arr, N))
