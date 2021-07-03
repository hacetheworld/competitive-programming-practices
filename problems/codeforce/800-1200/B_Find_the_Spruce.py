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


def Solution(grid, n, m):
    # Write Your Code Here
    temp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        star = 0
        for j in range(m):
            if grid[i][j] == "*":
                temp[i][j] += star+1
                star += 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "*":
                needstar = 3
                ans += 1
                k = i+1
                l = j-1
                r = j+1
                while k < n and l >= 0 and r < m:
                    lstar = temp[k][l]
                    rstar = temp[k][r]
                    res = (rstar-lstar)+1
                    if grid[k][l] != "*" or grid[k][r] != "*" or res != needstar:
                        break
                    needstar += 2
                    ans += 1
                    k += 1
                    l -= 1
                    r += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        grid = [get_string() for _ in range(n)]
        Solution(grid, n, m)


# calling main Function
if __name__ == '__main__':
    main()
