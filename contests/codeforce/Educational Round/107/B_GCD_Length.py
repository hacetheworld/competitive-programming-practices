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


def Solution(a, b, c):
    # Write Your Code Here
    a1 = "1"
    b1 = "1"
    c1 = "1"
    for i in range(a-1):
        a1 += "0"
    for i in range(b-1):
        b1 += "0"

    for i in range(c-1):
        c1 += "0"
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    if (c1) == 1:
        print((a1)+1 if a1 % 2 == 0 else (a1), (b1))
    else:
        while a1 % c1 != 0:
            a1 += 1
        print(a1, end=" ")
        while b1 % c1 != 0:
            b1 += 1
        print(b1-10 if b1 % 10 != 0 else b1+10)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, b, c = get_ints_in_variables()
        Solution(a, b, c)


# calling main Function
if __name__ == '__main__':
    main()
