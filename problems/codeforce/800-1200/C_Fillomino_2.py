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


def helper(ans, i, j, n, v, cnt):
    if i < 0 or i >= n or j < 0 or j >= n or ans[i][j] != -1 or cnt["cnt"] == 0:
        return
    ans[i][j] = v
    cnt["cnt"] -= 1
    helper(ans, i+1, j, n, v, cnt)
    helper(ans, i, j-1, n, v, cnt)


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()

    ans = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        cnt = {}
        cnt["cnt"] = arr[i]
        helper(ans, i, i, n, arr[i], cnt)
    for v in ans:
        for c in v:
            if c == -1:
                continue
            print(c, end=" ")
        print()


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
