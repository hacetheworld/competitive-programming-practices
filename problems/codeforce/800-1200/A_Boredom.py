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


def helper(hm, cur, prev2):
    prev = cur-1
    if prev in hm:
        if prev2 in hm:
            if hm[cur]+hm[prev2] < hm[prev]:
                return prev
        else:
            if hm[cur] < hm[prev]:
                return prev
    return cur


def findPrev(arr, i, el):
    n = len(arr)
    cnt = 0
    for j in range(i, n):
        if el != arr[j]:
            el = arr[j]
            cnt += 1
        if cnt == 2:
            return el
    return -1


def Solution(arr, n):
    # Write Your Code Here
    hm = {}
    for v in arr:
        if v in hm:
            hm[v] += v
        else:
            hm[v] = v
    mx = max(arr)
    dp=[0 for _ in range(mx+1)]
    if 1 in hm:
        dp[1]=hm[1]
    else:
        dp[1]=0
    for i in range(2,mx+1):
        t=dp[i-2]
        if i in hm:
            t+=hm[i]
        dp[i]=max(dp[i-1],t)

    print(dp[mx])


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
