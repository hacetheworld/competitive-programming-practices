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


def canMake(a, i, n, mx, hm):
    for j in range(mx):
        if not j in hm:
            return False
    return True


def nextMx(a, i, n):
    l = 0
    r = n+1
    ans = 0
    hm = {}
    for j in range(i, n):
        hm[a[j]] = True
    # print(hm, "hm")
    while l <= r:
        mid = (l+r)//2
        if canMake(a, i, n, mid, hm):
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans


def Solution(a, n):
    # Write Your Code Here
    hm = {}
    suff = []
    mx = 0 if a[-1] != 0 else 1
    for i in range(n-1, -1, -1):
        if not a[i] in hm or a[i] == mx:
            hm[a[i]] = True
            while mx in hm:
                mx += 1
        hm[a[i]] = True
        suff.append(mx)
    i = 0
    ans = []
    # print(suff)
    while i < n:
        mx = suff[n-i-1]
        hm = {}
        ans.append(mx)
        # print(i, "ii")
        cnt = 0
        while i < n:
            if a[i] < mx and not a[i] in hm:
                cnt += 1
            hm[a[i]] = True
            if cnt == mx:
                break
            i += 1
        i += 1

    print(len(ans))
    print(*ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        Solution(a, n)


# calling main Function
if __name__ == '__main__':
    main()
