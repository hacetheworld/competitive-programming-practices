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


def Solution(a, b, n, x):
    # Write Your Code Here
    a = sorted(a)
    b = sorted(b, reverse=True)
    flag = False
    for i in range(n):
        if a[i]+b[i] > x:
            flag = True
            break
    print("NO") if flag else print("YES")


def main():
    # Take input Here and Call solution function
    tc = get_int()
    for t in range(tc):
        n, x = get_ints_in_variables()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, n, x)
        if t != tc-1:
            input()


# calling main Function
if __name__ == '__main__':
    main()
