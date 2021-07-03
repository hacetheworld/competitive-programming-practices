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
    sheep = 0
    for c in s:
        if c == "*":
            sheep += 1
    md = (sheep+1)//2
    ct = 0
    idx = 0
    for c in s:
        if c == "*":
            ct += 1
            if ct == md:
                break
        idx += 1
    ans = 0
    tmp = 0
    ct = idx
    for i in range(ct-1, -1, -1):
        if s[i] == "*":
            ans += tmp
        else:
            tmp += 1
    tmp = 0
    for i in range(ct, n):
        if s[i] == "*":
            ans += tmp
        else:
            tmp += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        Solution(get_string(), n)


# calling main Function
if __name__ == '__main__':
    main()
