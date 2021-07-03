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
    hm = {}
    est = 0
    nrt = 0
    ans = 0
    t1 = 0
    t2 = 0
    for c in s:
        nrt = t1
        est = t2
        if c == "S":
            t1 -= 1
        elif c == "W":
            t2 -= 1
        if c == "N":
            t1 += 1
        elif c == "E":
            t2 += 1
        if hm.get((nrt+t1, est+t2)):
            ans += 1
        else:
            hm[(nrt+t1, est+t2)] = True
            ans += 5
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
