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


def Solution():
    # Write Your Code Here
    for _ in range(get_int()):
        x1, p1 = get_ints_in_variables()
        x2, p2 = get_ints_in_variables()
        if p1 > p2:
            t = p1-p2
            for _ in range(t):
                x1 *= 10
                if x1 >= x2:
                    break
        else:
            t = p2-p1
            for _ in range(t):
                x2 *= 10
                if x2 >= x1:
                    break
        # print(x2, x1)
        if x1 > x2:
            print(">")
        elif x1 == x2:
            print("=")
        else:
            print("<")


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
