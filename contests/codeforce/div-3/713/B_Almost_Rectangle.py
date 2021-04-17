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
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        grid = [[c for c in get_string()] for _ in range(n)]
        r1, c1, r2, c2, = 1, 1, 1, 1
        flag = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "*":
                    if flag:
                        r1, c1 = i, j
                        flag = False
                    else:
                        r2, c2 = i, j
        if c1 == c2:
            grid[r1][(c1+1) % n] = "*"
            grid[r2][(c2+1) % n] = "*"
        elif r1 == r2:
            grid[(r1+1) % n][c2] = "*"
            grid[(r2+1) % n][c1] = "*"
        else:
            grid[r1][c2] = "*"
            grid[r2][c1] = "*"
        for i in range(n):
            for j in range(n):
                print(grid[i][j], end="")
            print()


# calling main Function
if __name__ == '__main__':
    main()
