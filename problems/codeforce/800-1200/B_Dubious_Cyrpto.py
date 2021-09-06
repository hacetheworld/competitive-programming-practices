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


def Solution(l, r, m):
    # Write Your Code Here
    diff = r-l
    a, b, c = l, l, l
    for i in range(l, r+1):
        m1 = m % i
        m2 = i-(m % i)
        if(i <= m and m1 <= diff):
            a = i
            b = r
            c = r-m1
            break
        elif(m2 <= diff):
            a = i
            b = r-m2
            c = r
            break
    print(a, b, c)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        l, r, m = get_ints_in_variables()
        Solution(l, r, m)


# calling main Function
if __name__ == '__main__':
    main()
