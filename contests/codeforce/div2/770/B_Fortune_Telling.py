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
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, x, y = get_ints_in_variables()
        a = get_ints_in_list()
        sm = sum(a)
        if y % 2 == 0:
            if sm % 2 == 0 and (x+3) % 2 == 0 or sm % 2 and (x+3) % 2:
                print("Bob")
            else:
                print("Alice")
        else:
            if sm % 2 == 0 and (x+3) % 2 == 1 or sm % 2 and (x+3) % 2 == 0:
                print("Bob")
            else:
                print("Alice")


# calling main Function
if __name__ == '__main__':
    main()
