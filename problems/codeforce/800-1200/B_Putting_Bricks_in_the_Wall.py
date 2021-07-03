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


def Solution(grid, n):
    # Write Your Code Here
    a = grid[0][1]
    b = grid[1][0]
    c = grid[-1][n-2]
    d = grid[n-2][-1]
    if(a == b):
        if (c == d and c != a):
            print(0)
        elif (c == d and c == a):
            print(2)
            print(n, n-1)
            print(n-1, n)

        elif (c != d):
            if (c == a):
                print(1)
                print(n, n-1)
            else:
                print(1)
                print(n-1, n)
    else:
        if (c == d):
            if (c == a):
                print(1)
                print(1, 2)
            elif (c == b):
                print(1)
                print(2, 1)

        else:
            if (c == a):
                print(2)
                print(1, 2)
                print(n-1, n)
            elif (c == b):
                print(2)
                print(2, 1)
                print(n-1, n)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        grid = [[c for c in get_string()] for _ in range(n)]
        Solution(grid, n)


# calling main Function
if __name__ == '__main__':
    main()
