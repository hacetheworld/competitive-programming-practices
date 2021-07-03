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
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 4:
                print("NO")
                return
    n -= 1
    m -= 1
    if grid[0][0] > 2 or grid[n][0] > 2 or grid[n][m] > 2 or grid[0][m] > 2:
        print("NO")
        return

    if max(grid[0]) > 3 or max(grid[n]) > 3:
        print("NO")
        return
    mx = -1
    for i in range(n):
        mx = max([grid[i][0], grid[i][-1], mx])
    if mx > 3:
        print("NO")
        return
    print("YES")
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or i == n:
                if j == 0 or j == m:
                    grid[i][j] = 2
                else:
                    grid[i][j] = 3
            else:
                if j == 0 or j == m:
                    grid[i][j] = 3
                else:
                    grid[i][j] = 4
    for i in range(n+1):
        for j in range(m+1):
            print(grid[i][j], end=" ")
        print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        grid = get_list_of_list(n)
        Solution(grid, n, m)


# calling main Function
if __name__ == '__main__':
    main()
