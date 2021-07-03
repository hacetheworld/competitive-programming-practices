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


def Solution(s):
    # Write Your Code Here
    c0 = 0
    c1 = 0
    ans = 0
    for c in s:
        if c == "0":
            c0 += 1
            c1 = 0
            ans += c0
        elif c == "1":
            c1 += 1
            c0 = 0
            ans += c1
        else:
            c0 += 1
            c1 += 1
            ans += max(c0, c1)
        tmp = c0
        c0 = c1
        c1 = tmp
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
