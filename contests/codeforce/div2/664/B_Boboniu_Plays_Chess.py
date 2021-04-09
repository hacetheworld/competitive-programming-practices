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


def isValid(n, m, x, y):
    return not (x > n or x <= 0 or y > m or y <= 0)


def traverse(n, m, x, y):
    for _ in range(1, n+1):
        for _ in range(1, m+1):
            print(x, y)
            y += 1
            if y > m:
                y = 1
        x += 1
        y -= 1
        if y == 0:
            y = m
        if x > n:
            x = 1


def Solution():
    # Write Your Code Here
    n, m, x, y = get_ints_in_variables()
    traverse(n, m, x, y)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
