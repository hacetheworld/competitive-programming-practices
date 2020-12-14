def Solution(arr, countsArr):
    # Solution
    for i in range(len(arr)):
        if arr[i] == -1:
            newVal = countsArr[i]//i
            countsArr[i+1] = countsArr[i]+newVal
            print(newVal, end=" ")

        else:
            countsArr[i+1] = countsArr[i]+arr[i]
            print(arr[i], end=" ")


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    countsArr = [0 for _ in range(N+1)]
    Solution(arr, countsArr)
