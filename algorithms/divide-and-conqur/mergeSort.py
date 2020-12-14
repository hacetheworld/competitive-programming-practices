def mergeSort(arr):
    mergeSortHelper(arr, 0, len(arr)-1)


def mergeSortHelper(arr, l, r):
    if l < r:
        mid = (l+r)//2
        mergeSortHelper(arr, l, mid)
        mergeSortHelper(arr, mid+1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    temp = [None]*(r+1)
    s1 = l
    k = l
    s2 = mid+1
    while s1 <= mid and s2 <= r:
        if arr[s1] < arr[s2]:
            temp[k] = arr[s1]
            s1 += 1
        else:
            temp[k] = arr[s2]
            s2 += 1
        k += 1
    while s1 <= mid:
        temp[k] = arr[s1]
        s1 += 1
        k += 1
    while s2 <= r:
        temp[k] = arr[s2]
        s2 += 1
        k += 1
    for i in range(len(temp)):
        if temp[i]:
            arr[i] = temp[i]


arr = list(map(int, input().split()))
mergeSort(arr)
print(arr)
