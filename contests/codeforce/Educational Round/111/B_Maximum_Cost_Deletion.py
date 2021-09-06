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


def Solution(s, n, a, b):
    # Write Your Code Here
    if b >= 0 or len(s) == 1:
        print(n*(a+b))
        return
    cnt = 0
    i = 0
    if s[i] == "1":
        while i < n:
            if s[i] == "0":
                cnt += 1
                while i < n-1 and s[i] == s[i+1]:
                    i += 1
            i += 1
    else:
        while i < n:
            if s[i] == "1":
                cnt += 1
                while i < n-1 and s[i] == s[i+1]:
                    i += 1
            i += 1
    print((a*n)+((cnt+1)*b))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, a, b = get_ints_in_variables()
        s = get_string()
        Solution(s, n, a, b)


# calling main Function
if __name__ == '__main__':
    main()
