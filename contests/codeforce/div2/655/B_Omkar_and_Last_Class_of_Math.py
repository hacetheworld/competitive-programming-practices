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


def Solution(n):
    # Write Your Code Here
    if n % 2 == 0:
        print(n//2, n//2)
    else:
        l = 2
        while l*l <= n:
            if n % l == 0:
                print(n//l, n-(n//l))
                return
            l += 1
        print(1, n-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        Solution(n)


# calling main Function
if __name__ == '__main__':
    main()
