def mergeSort(arr):
    return mergeSortHelper(arr, 0, len(arr)-1)


def mergeSortHelper(arr, l, r):
    reverse_pair_count = 0
    if l < r:
        mid = (l+r)//2
        reverse_pair_count += mergeSortHelper(arr, l, mid)
        reverse_pair_count += mergeSortHelper(arr, mid+1, r)
        reverse_pair_count += merge(arr, l, mid, r)
    return reverse_pair_count


def merge(arr, l, mid, r):
    reverse_pair_count = 0
    j = mid+1
    for i in range(l, mid+1):
        while j <= r and (arr[i] > (2*arr[j])):
            j += 1
        reverse_pair_count += (j-(mid+1))
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
    return reverse_pair_count


arr = list(map(int, input().split(",")))

print(mergeSort(arr))
