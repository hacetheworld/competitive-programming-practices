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


def Solution(grid, r, c):
    # Write Your Code Here
    mx = grid[0][0]
    for i in range(r):
        for j in range(c):
            if grid[i][j] > mx:
                mx = grid[i][j]
    op = [[grid[i][j] for j in range(c)] for i in range(r)]
    while True:
        f = 1
        for i in range(r):
            for j in range(c):
                if op[i][j] == mx:
                    f = 0
                    if i+1 < r:
                        op[i+1][j] = max(op[i+1][j], mx-1)
                    if j+1 < c:
                        op[i][j+1] = max(op[i][j+1], mx-1)
                    if i-1 >= 0:
                        op[i-1][j] = max(op[i-1][j], mx-1)
                    if j-1 >= 0:
                        op[i][j-1] = max(op[i][j-1], mx-1)
        mx -= 1
        if f:
            break
    ans = 0
    # print(op)
    for i in range(r):
        for j in range(c):
            ans += abs(op[i][j]-grid[i][j])
    return ans


def main():
    # Take input Here and Call solution function
    for t in range(get_int()):
        r, c = get_ints_in_variables()
        grid = get_list_of_list(r)
        print("Case #{}: {}".format(t+1, Solution(grid, r, c)))


# calling main Function
if __name__ == '__main__':
    main()
