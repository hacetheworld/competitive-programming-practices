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


def Solution(n, a, b):
    # Write Your Code Here
    if a == 1:
        if b == 1 or n % b == 1:
            print("YES")
            return
        else:
            print("NO")
            return
    if b == 1:
        print("YES")
        return
    flag = False
    p = 1
    while p <= n:
        if (n-p) % b == 0:
            flag = True
            break
        p *= a
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, a, b = get_ints_in_variables()
        Solution(n, a, b)


# calling main Function
if __name__ == '__main__':
    main()
