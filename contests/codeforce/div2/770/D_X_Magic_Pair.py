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


def swap(a, b):
    if a > b:
        return [b, a]
    else:
        return [a, b]


def Solution(a, b, x):
    # Write Your Code Here
    if a > b:
        t = swap(a, b)
        a, b = t[0], t[1]

    while a:
        if a == x or b == x:
            print("YES")
            return True
        elif x > a and x < b and x % a == b % a:
            print("YES")
            return True
        b = b % a
        t = swap(a, b)
        a, b = t[0], t[1]
    print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, b, x = get_ints_in_variables()
        Solution(a, b, x)


# calling main Function
if __name__ == '__main__':
    main()
