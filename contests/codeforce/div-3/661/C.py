import math


def Solution(arr, n):
    if n == 1:
        return 0
    arr = sorted(arr)
    s = arr[n-1]+arr[n-2]
    count = 0
    for i in range(max(arr), s+1):
        l = 0
        r = n-1
        temp = 0
        while l < r:
            if (arr[l]+arr[r]) == i:
                temp += 1
                l += 1
                r -= 1
            elif (arr[l]+arr[r]) > i:
                r -= 1
            else:
                l += 1

        count = max(count, temp)

    return count


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr,  N))
# print(op)
#
