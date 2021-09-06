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


def Solution(s, t):
    # Write Your Code Here
    if len(t) > len(s):
        print("NO")
        return
    i = len(s)-1
    j = len(t)-1

    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            j -= 1
            i -= 1
        else:
            i -= 2
    # print("j", j, "i", i)
    if j == -1:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s = get_string()
        t = get_string()
        Solution(s, t)


# calling main Function
if __name__ == '__main__':
    main()
