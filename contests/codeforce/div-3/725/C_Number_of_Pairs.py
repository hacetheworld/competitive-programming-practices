# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------------- SOLUTION FUNCTION ------------------


def helperFun(arr, n, l, r):

    i = 0
    j = n-1
    sid = -1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] >= l:
            j = mid-1
            sid = mid
        else:
            i = mid + 1

    return sid


def helperFun2(arr, n, l, r):

    i = 0
    j = n-1
    sid = -1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] <= r:
            i = mid+1
            sid = mid
        else:
            j = mid-1
    return sid


def Solution(arr, n, l, r):
    # Write Your Code Here
    arr = sorted(arr)
    ans = 0
    # print(arr)
    for i in range(n-1, -1, -1):
        if arr[i] >= r or r-arr[i] > arr[i]:
            continue
        l1 = helperFun(arr, i, abs(l-arr[i]), r-arr[i])
        r1 = helperFun2(arr, i, abs(l-arr[i]), r-arr[i])
        if l1 != -1 and r1 != -1:
            tmp = (r1-l1)+1
            # print(l1, r1)
            if tmp >= 2:
                ans += ((tmp*(tmp-1))//2)
            elif tmp == 1:
                ans += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, l, r = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, l, r)


# calling main Function
if __name__ == '__main__':
    main()
