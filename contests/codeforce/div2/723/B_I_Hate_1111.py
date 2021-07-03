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


def Solution(x):
    # Write Your Code Here
    flag = False
    while x > 0:
        if x % 11 == 0 or x % 111 == 0:
            flag = True
            break
        x -= 11
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
