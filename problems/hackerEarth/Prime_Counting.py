def Solution(arr, N):
    # Solution
    L, R = 0, 0
    for i in range(len(arr)):
        interval = arr[i]
        if interval[0] > L


for t in range(int(input())):
    N = int(input())
    intervals = []
    for _ in range(N):
        interval = list(map(int, input().split()))
        intervals.append(interval)
    # strArr = [input() for _ in range(N)]
    print(Solution(intervals, N))
