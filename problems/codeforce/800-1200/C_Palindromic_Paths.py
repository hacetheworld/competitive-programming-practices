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


def Solution(grid, n, m):
    # Write Your Code Here
    p = [0 for _ in range(n+m)]
    q = [0 for _ in range(n+m)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                p[i+j] += 1
            else:
                q[i+j] += 1
    r = (n+m-2)//2
    ans = 0
    for i in range(r+1):
        if i != r or (n+m) % 2 != 0:
            x = p[i]+p[n+m-2-i]
            y = q[i]+q[n+m-2-i]
            ans += (min(x, y))
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        grid = get_list_of_list(n)
        Solution(grid, n, m)


# calling main Function
if __name__ == '__main__':
    main()
