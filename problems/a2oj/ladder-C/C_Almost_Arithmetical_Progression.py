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


def findSubsequence(arr, a, b, strt, n):
    el = a
    cnt = 0
    for i in range(strt+1, n):
        if arr[i] == el:
            cnt += 1
            el = b if el == a else a
    return cnt


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    ans = 0
    hm = {}
    if n >= 3:
        for i in range(n):
            if arr[i] in hm:
                continue
            else:
                hm[arr[i]] = True
            for j in range(i+1, n):
                ans = max(ans, findSubsequence(arr, arr[i], arr[j], j, n)+2)
    else:
        ans = n
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
