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


def Solution(s, lettrs, n, k):
    # Write Your Code Here
    ans = 0
    i = 0
    prev = 0
    while i < n:
        while i < n and s[i] in lettrs:
            i += 1
        t = (i)-prev
        # print(i, "kkkk")
        ans += ((t*(t+1))//2)
        prev = i+1
        i += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    s = get_string()
    lettrs = [c for c in get_string()]
    Solution(s, lettrs, n, k)


# calling main Function
if __name__ == '__main__':
    main()
