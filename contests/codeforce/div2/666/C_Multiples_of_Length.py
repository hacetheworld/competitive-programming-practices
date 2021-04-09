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

# -------------- SOLUTION FUNCTION ------------------


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    if n == 1:
        print(1, 1)
        print(-arr[0])
        print(1, 1)
        print(0)
        print(1, 1)
        print(0)
        return

    print(1, n-1)
    for i in range(n-1):
        print(arr[i]*(n-1), end=" ")
        arr[i] = arr[i]*n
    print()
    print(n, n)
    print(arr[n-1]*(n-1))
    arr[n-1] = arr[n-1]*n
    print(1, n)
    for i in range(n):
        print(-arr[i], end=" ")
        arr[i] = 0
    print()


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
