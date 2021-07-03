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


def Solution(n, k):
    # Write Your Code Here
    if k > n:
        print("NO")
        return
    t1 = n-(k-1)
    t2 = n-(2*(k-1))
    if t1 > 0 and t1 % 2 == 1:
        print("YES")
        print(t1, end=" ")
        for _ in range(k-1):
            print(1, end=" ")
        print()
    elif t2 > 0 and t2 % 2 == 0:
        print("YES")
        print(t2, end=" ")
        for _ in range(k-1):
            print(2, end=" ")
        print()
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()
