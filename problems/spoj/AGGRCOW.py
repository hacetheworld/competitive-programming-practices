def Solution(arr, N, C):
    # Solution
    l = 0
    r = arr[-1]-arr[0]
    mid = (l+r)//2
    while l <= r:
        if canPlaceCow(arr, C, mid):
            l = mid+1
        else:
            r = mid-1
        mid = (l+r)//2
    return mid


def canPlaceCow(arr, C, diff):
    prev_cow_idx = arr[0]
    C -= 1
    for i in range(1, len(arr)):
        if (arr[i]-prev_cow_idx) >= diff:
            prev_cow_idx = arr[i]
            C -= 1
    return C <= 0


for t in range(int(input())):
    N, C = map(int, input().split())
    arr = sorted([int(input()) for _ in range(N)])
    # print(arr)
    # strArr = [input() for _ in range(N)]
    print(Solution(arr, N, C))
