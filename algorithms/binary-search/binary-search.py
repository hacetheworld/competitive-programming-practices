def binarySearch(arr, key):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left+((right-left)//2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid+1
        else:
            right = mid-1
    return -1


def binarySearchLowerBound(arr, key):
    left = 0
    right = len(arr)-1
    res = -1
    while left <= right:
        mid = left+((right-left)//2)
        if arr[mid] < key:
            left = mid+1
        else:
            res = arr[mid]
            right = mid-1
    return res


def binarySearchUpparBound(arr, key):
    left = 0
    right = len(arr)-1
    res = -1
    while left <= right:
        mid = left+((right-left)//2)
        if arr[mid] < key:
            res = mid
            left = mid+1
        else:
            right = mid-1
    return res


arr = list(map(int, input().split()))
key = int(input())
print(binarySearchUpparBound(arr, key))
