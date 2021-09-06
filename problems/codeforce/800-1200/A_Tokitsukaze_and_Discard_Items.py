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


def bst(mxp, k, cnt, el):
    l = 1
    r = mxp
    ans = 1
    while l <= r:
        mid = (l+r)//2
        if mid*k >= el-cnt:
            ans = mid
            r = mid-1
        else:
            l = mid+1
    return ans


def Solution(arr, n, m, k):
    # Write Your Code Here
    ans = 0
    cnt = 0
    i = 0
    while i < m:
        pos = (myceil(arr[i]-cnt, k)*k)+cnt
        while i < m and pos >= arr[i]:
            i += 1
            cnt += 1
        ans += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, m, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, m, k)


# calling main Function
if __name__ == '__main__':
    main()
