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


def Solution(a, n, k):
    # Write Your Code Here
    if n == 1:
        if a[0] <= k:
            print(0)
        else:
            print(a[0]-k)
        return
    if sum(a) <= k:
        print(0)
        return
    a = sorted(a)
    pref = [0]
    for v in a:
        pref.append(pref[-1]+v)
    pref.pop(0)
    l = 0
    r = sum(a)
    ans = 0
    while l <= r:
        mid = (l+r)//2
        f = 0
        for i in range(n):
            if mid-i >= 0 and pref[n-i-1]-a[0]+(a[0]-mid+i)*(i+1) <= k:
                f = 1
                break
        if f:
            ans = mid
            r = mid-1
        else:
            l = mid+1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        a = get_ints_in_list()
        Solution(a, n, k)


# calling main Function
if __name__ == '__main__':
    main()
