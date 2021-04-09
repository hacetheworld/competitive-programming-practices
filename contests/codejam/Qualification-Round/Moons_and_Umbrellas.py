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


def countBill(s, n, x, y):
    ans = 0
    for i in range(n-1):
        if (s[i] == "C" and s[i+1] == "J"):
            ans += x
        elif (s[i] == "J" and s[i+1] == "C"):
            ans += y
    return ans


def helper(s, n, x, y, i):
    if i >= n:
        return countBill(s, n, x, y)
    if s[i] != "?":
        return helper(s, n, x, y, i+1)
    else:
        s[i] = "C"
        r1 = helper(s, n, x, y, i+1)
        s[i] = "J"
        r2 = helper(s, n, x, y, i+1)
        s[i] = "?"
        return min(r1, r2)


def Solution(s, x, y):
    # Write Your Code Here
    n = len(s)
    s = [c for c in s]
    return helper(s, n, x, y, 0)


def main():
    # Take input Here and Call solution function
    for t in range(get_int()):
        x, y, s = sys.stdin.readline().strip().split()
        x = int(x)
        y = int(y)
        print("Case #{}: {}".format(t+1, Solution(s, x, y)))


# calling main Function
if __name__ == '__main__':
    main()
