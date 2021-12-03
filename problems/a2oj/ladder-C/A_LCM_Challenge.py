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


def Solution(n):
    # Write Your Code Here
    if n <= 3:
        ans = 1
        for i in range(1, n+1):
            ans *= i
        print(ans)

    else:
        ans = 1
        if n % 2:
            ans = n*(n-1)*(n-2)
        else:
            if n % 3 == 0:
                ans = (n-1)*(n-2)*(n-3)
            else:
                ans = n*(n-1)*(n-3)
        print(ans)


def main():
    # Take input Here and Call solution function
    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
