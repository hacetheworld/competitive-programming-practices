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


def Solution(arr, n, k):
    # Write Your Code Here
    cnt = 0
    for i in range(1, n):
        if arr[i-1]+arr[i] < k:
            cnt += (k-(arr[i-1]+arr[i]))
            arr[i] += (k-(arr[i-1]+arr[i]))

    print(cnt)
    print(*arr)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
