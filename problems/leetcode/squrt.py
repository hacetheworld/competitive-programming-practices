def binarySearch(n):
    left = 0
    right = n
    res = 0
    while left <= right:
        mid = left+((right-left)//2)
        sqr = mid*mid
        if sqr == n:
            return mid
        elif sqr < n:
            res = mid
            left = mid+1
        else:
            right = mid-1
    return res


print(binarySearch(int(input())))
