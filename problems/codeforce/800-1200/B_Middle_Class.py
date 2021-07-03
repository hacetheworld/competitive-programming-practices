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


def Solution(arr, n, x):
    # Write Your Code Here
    s = 0
    arr = sorted(arr)
    ans = 1
    for i in range(n-1, -1, -1):
        if ((s+arr[i])//ans) >= x:
            ans += 1
            s += arr[i]
    print(ans-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, x = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, x)


# calling main Function
if __name__ == '__main__':
    main()
