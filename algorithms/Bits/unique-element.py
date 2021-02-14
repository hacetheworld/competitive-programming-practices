def unique(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        el = arr[i]
        res = res ^ el
    return res


print(unique([1, 2, 3, 1, 5, 2, 3, 5, 7]))
