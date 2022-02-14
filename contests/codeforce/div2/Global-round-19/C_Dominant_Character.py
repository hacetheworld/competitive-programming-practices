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


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        ans = float("inf")
        for i in range(n):
            if s[i] == "a":
                for j in [1, 2, 3, 6]:
                    if i+j < n and s[i+j] == "a":
                        a, b, c = 2, 0, 0
                        for k in range(i+1, i+j):
                            if s[k] == "b":
                                b += 1
                            elif s[k] == "a":
                                a += 1
                            else:
                                c += 1
                        if a > b and a > c:
                            ans = min(ans, j+1)
        print(-1 if ans == float("inf") else ans)


# calling main Function
if __name__ == '__main__':
    main()
