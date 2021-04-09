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
    id1, id2 = 1, 1
    for i in range(r):
        for j in range(c):
            if mx < grid[i][j]:
                mx = grid[i][j]
                id1, id2 = i+1, j+1
    # print(s, mx)
    ans = 0
    for i in range(r):
        for j in range(c):
            cur = abs(i+1-id1)+abs(j+1-id2)
            if mx-cur > 0:
                v = mx-cur
                ans += abs(v-grid[i][j])
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
