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


def median(a, b, c, d):
    pair = sorted([a, b, c, d])
    return((pair[1]+pair[2])//2)


def Solution(grid, n, m):
    # Write Your Code Here
    ans = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            a, b, c, d = grid[i][j], grid[(n+1) -
                                          i][j], grid[i][(m+1)-j], grid[(n+1)-i][(m+1)-j]
            tmp = median(a, b, c, d)
            ans[i][j] = tmp
    res = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            res += abs(grid[i][j]-ans[i][j])
    print(res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        grid = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            inp = sys.stdin.readline().strip().split()
            for j in range(m):
                grid[i][j+1] = int(inp[j])
        Solution(grid, n, m)


# calling main Function
if __name__ == '__main__':
    main()
