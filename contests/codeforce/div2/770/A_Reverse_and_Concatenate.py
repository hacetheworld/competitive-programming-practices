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


def isplaindrome(s):
    n = len(s)
    i = 0
    j = n-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        if k == 0 or isplaindrome(s):
            print(1)
        else:
            print(2)


# calling main Function
if __name__ == '__main__':
    main()
