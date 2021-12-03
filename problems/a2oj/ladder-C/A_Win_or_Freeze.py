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


def getFirstD(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return i
    return n


def Solution(n):
    # Write Your Code Here
    f = getFirstD(n)
    if f == n or n == 1:
        print(1)
        print(0)
    else:
        s = getFirstD(n//f)
        if s*f == n:
            print(2)
        else:
            print(1)
            print(f*s)


def main():
    # Take input Here and Call solution function
    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
