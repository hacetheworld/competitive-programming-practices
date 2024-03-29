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


def Solution(s, n, t):
    # Write Your Code Here
    s = [c for c in s]
    for _ in range(t):
        i = 0
        while i < n:
            if s[i] == "B" and i < n-1 and s[i+1] != s[i]:
                tmp = s[i]
                s[i] = s[i+1]
                s[i+1] = tmp
                i += 1
            i += 1
    print("".join(s))


def main():
    # Take input Here and Call solution function
    n, t = get_ints_in_variables()
    s = get_string()
    Solution(s, n, t)


# calling main Function
if __name__ == '__main__':
    main()
