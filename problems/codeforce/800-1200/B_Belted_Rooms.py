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


def Solution(s, n):
    # Write Your Code Here
    num_ = 0
    numf = 0
    numb = 0
    for c in s:
        if c == "-":
            num_ += 1
        elif c == ">":
            numf += 1
        else:
            numb += 1
    if numb == 0 or numf == 0:
        print(n)
    else:
        ans = 0
        if s[0] == "-" or s[-1] == "-":
            ans += 1
        for i in range(1, n):
            if s[i-1] == "-" or s[i] == "-":
                ans += 1
        print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()
