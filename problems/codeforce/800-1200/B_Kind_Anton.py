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


def Solution(a, b, n):
    # Write Your Code Here
    if a[0] != b[0]:
        print("NO")
        return
    neg = -1
    pos = -1
    for i in range(n):
        if neg == -1 and a[i] < 0:
            neg = i
        if pos == -1 and a[i] > 0:
            pos = i
    flag = True
    for i in range(n-1, -1, -1):
        if a[i] != b[i]:
            if (a[i] < b[i] and pos != -1 and pos < i) or (a[i] > b[i] and neg != -1 and neg < i):
                continue
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, n)


# calling main Function
if __name__ == '__main__':
    main()
