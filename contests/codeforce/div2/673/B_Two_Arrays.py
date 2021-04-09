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


def Solution(arr, n, t):
    # Write Your Code Here
    f = 1
    for v in arr:
        if t % 2 == 0 and v == t//2:
            r = f
            if f:
                f = 0
            else:
                f = 1
        elif 2*v > t:
            r = 1
        else:
            r = 0
        print(r, end=" ")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, t = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, t)


# calling main Function
if __name__ == '__main__':
    main()
