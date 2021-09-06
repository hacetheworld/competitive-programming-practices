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


def Solution(s):
    # Write Your Code Here
    n = len(s)
    lens = []
    i = 0
    while i < n:
        tmp = 1
        c = s[i]
        i += 1
        while i < n and s[i] == s[i-1]:
            i += 1
            tmp += 1
        lens.append([tmp, c])
    # print(lens, "before")
    for i in range(1, len(lens)):
        if lens[i][0] == 2:
            if lens[i-1][0] >= 2:
                lens[i][0] = 1
        elif lens[i][0] > 2:
            if lens[i-1][0] >= 2:
                lens[i][0] = 1
            else:
                lens[i][0] = 2
    lens[0][0] = min(lens[0][0], 2)
    for v in lens:
        for _ in range(v[0]):
            print(v[1], end="")
    print()


def main():
    # Take input Here and Call solution function
    Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
