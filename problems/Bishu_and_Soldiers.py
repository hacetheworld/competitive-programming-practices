def Solution(arr, p):
    # Solution
    if p >= len(arr):
        return len(arr)
    l = 0
    r = len(arr)
    mid = (l+r)//2
    while l <= r:
        if arr[mid] == p:
            return mid+1
        elif arr[mid] > p:
            r = mid-1
        else:
            l = mid+1
        mid = (l+r)//2
    return r+1


N = int(input())
arr = sorted(list(map(int, input().split())))
Q = int(input())
prefix = [0]
for i in range(N):
    prefix.append(prefix[i]+arr[i])
for _ in range(Q):
    p = int(input())
    idx = Solution(arr, p)
    print(idx, prefix[idx])
