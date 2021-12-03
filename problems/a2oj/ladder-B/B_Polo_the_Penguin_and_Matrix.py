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


def Solution(arr1, n, m, d):
    # Write Your Code Here
    arr = []
    for itm in arr1:
        for c in itm:
            arr.append(c)
    arr = sorted(arr)
    equalto = arr[len(arr)//2]
    ans = 0
    rem = arr[0] % d
    flg = True
    for v in arr:
        if v % d != rem:
            flg = False
            break
        ans += (abs(equalto-v)//d)
        if not flg:
            break
    if flg:
        print(ans)
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    n, m, d = get_ints_in_variables()
    arr = get_list_of_list(n)
    Solution(arr, n, m, d)


# calling main Function
if __name__ == '__main__':
    main()
