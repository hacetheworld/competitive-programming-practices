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


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    res = []
    freq = {}
    for v in arr:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1
    el = -1
    cnt = 0
    for key in freq:
        if freq[key] > cnt:
            el = key
            cnt = freq[key]

    idx = arr.index(el)
    for i in range(idx+1, n):
        diff = abs(arr[i]-arr[i-1])
        if arr[i] < el:
            arr[i] += diff
            res.append([1, i+1, i])
        elif arr[i] > el:
            arr[i] -= diff
            res.append([2, i+1, i])
    for i in range(idx-1, -1, -1):
        diff = abs(arr[i]-arr[i+1])
        if arr[i] < el:
            arr[i] += diff
            res.append([1, i+1, i+2])
        elif arr[i] > el:
            arr[i] -= diff
            res.append([2, i+1, i+2])
    print(len(res))
    for itm in res:
        print(*itm)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
