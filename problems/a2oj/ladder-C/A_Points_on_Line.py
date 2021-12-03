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


def Solution(arr, n, d):
    # Write Your Code Here
    i = 0
    j = 0
    ans = 0
    while i < n:
        while j < n and arr[j] <= arr[i] + d:
            j += 1
        k = j-i-1
        ans += ((k*(k-1))//2)
        i += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, d = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, d)


# calling main Function
if __name__ == '__main__':
    main()
