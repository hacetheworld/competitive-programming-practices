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
    a, b = get_ints_in_variables()
    gc = math.gcd(a, b)
    a = a//gc
    b = b//gc
    if abs(a-b) == 1:
        print("Equal")
        return
    n = a*b
    if a < b:
        a = (n/a)-1
        b = n/b
    else:
        a = (n/a)
        b = (n/b)-1
    if a > b:
        print("Dasha")
    elif a < b:
        print("Masha")
    else:
        print("Equal")


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
