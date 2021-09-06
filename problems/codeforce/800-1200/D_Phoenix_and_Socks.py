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


def Solution(arr, n, l, r):
    # Write Your Code Here
    left = {}
    right = {}
    for i in range(l):
        if arr[i] in left:
            left[arr[i]] += 1
        else:
            left[arr[i]] = 1
    for i in range(l, n):
        if arr[i] in right:
            right[arr[i]] += 1
        else:
            right[arr[i]] = 1
    for v in left:
        if left[v] <= 0:
            continue
        if v in right and right[v] > 0:
            mn = min(left[v], right[v])
            left[v] -= mn
            right[v] -= mn
    ans = 0
    if l < n//2:
        cnt = (n//2)-l
        ans += (cnt)
        for v in right:
            if right[v] <= 1:
                continue
            mn = min(right[v]//2, cnt)
            cnt -= mn
            right[v] -= (2*mn)
            if cnt == 0:
                break
        if cnt != 0:
            for v in right:
                if right[v] == 0:
                    continue
                mn = min(right[v], cnt)
                cnt -= mn
                right[v] -= mn
                if v in left:
                    left[v] += mn
                else:
                    left[v] = mn
                if cnt == 0:
                    break
    elif r < n//2:
        cnt = (n//2)-r
        ans += (cnt)
        for v in left:
            if left[v] <= 1:
                continue
            mn = min(left[v]//2, cnt)
            cnt -= mn
            left[v] -= (2*mn)
            if cnt == 0:
                break
        if cnt != 0:
            for v in left:
                if left[v] == 0:
                    continue
                mn = min(left[v], cnt)
                cnt -= mn
                left[v] -= mn
                if v in right:
                    right[v] += mn
                else:
                    right[v] = mn
                if cnt == 0:
                    break

    for v in left:
        if left[v] <= 0:
            continue
        if v in right and right[v] > 0:
            mn = min(left[v], right[v])
            left[v] -= mn
            right[v] -= mn
    counter = 0
    for v in left:
        if left[v] > 0:
            counter += left[v]
    print(ans+(counter))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, l, r = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, l, r)


# calling main Function
if __name__ == '__main__':
    main()
