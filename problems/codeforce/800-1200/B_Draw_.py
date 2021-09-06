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


def isEqual(a, b):
    return a[0] == b[0] and a[1] == b[1]


def Solution(arr, n):
    # Write Your Code Here
    lst = [0, 0]
    ans = 0
    for i in range(n):
        l = max(lst)
        r = min(arr[i])
        if l <= r:
            ans += (r+1-l)
            if i < n-1 and arr[i][0] == arr[i][1]:
                ans -= 1
        lst = arr[i]
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = []
    for _ in range(n):
        itm = get_ints_in_list()
        arr.append(itm)
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
