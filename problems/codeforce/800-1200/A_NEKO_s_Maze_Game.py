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


def Solution(n, q):
    # Write Your Code Here
    store = [[0 for _ in range(n)] for _ in range(2)]
    cnt = 0
    for _ in range(q):
        r, c = get_ints_in_variables()
        r -= 1
        c -= 1
        tmp = 1 if store[r][c] == 0 else -1
        store[r][c] = 1-store[r][c]
        for cell in range(-1, 2):
            if c+cell >= 0 and c+cell < n and store[1-r][c+cell]:
                cnt += tmp
        if cnt == 0:
            print("YES")
        else:
            print("NO")


def main():
    # Take input Here and Call solution function
    # for _ in range(get_int()):
    n, q = get_ints_in_variables()
    Solution(n, q)


# calling main Function
if __name__ == '__main__':
    main()
