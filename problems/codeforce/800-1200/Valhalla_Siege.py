def Solution(N, Q, wariors_strength, arrows):
    # Solution
    prefix_sum = [0]
    for strength in wariors_strength:
        prefix_sum.append(prefix_sum[-1]+strength)
    prefix_sum.pop(0)
    arrow_so_far = 0
    for arrow in arrows:
        arrow_so_far += arrow
        if arrow_so_far >= prefix_sum[-1]:
            print(N)
            arrow_so_far = 0
        else:
            idx = binarySearch_LowerBound(prefix_sum, arrow_so_far)
            print(N-idx)


def binarySearch_LowerBound(arr, key):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == key:
            return mid+1
        elif arr[mid] > key:
            r = mid-1
        else:
            l = mid+1
    return r+1


N, Q = map(int, input().split())
wariors_strength = list(map(int, input().split()))
arrows = list(map(int, input().split()))
# strArr = [input() for _ in range(N)]

Solution(N, Q, wariors_strength, arrows)
