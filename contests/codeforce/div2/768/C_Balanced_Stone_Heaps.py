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

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def helper(arr, n, k):
    tmp = [v for v in arr]
    for i in range(n-1, 1, -1):
        if tmp[i] < k:
            return False
        d = min(arr[i], tmp[i]-k)//3
        tmp[i-1] += d
        tmp[i-2] += (2*d)
    return tmp[0] >= k and tmp[1] >= k


def Solution(arr, n):
    # Write Your Code Here
    l = min(arr)
    r = max(arr)
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if helper(arr, n, mid):
            ans = max(ans, mid)
            l = mid+1
        else:
            r = mid-1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
