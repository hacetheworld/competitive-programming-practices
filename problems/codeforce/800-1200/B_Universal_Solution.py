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


def Solution(s):
    # Write Your Code Here
    freq = {}
    mxFreq = 0
    mxChar = ""
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
        if mxFreq < freq[c]:
            mxFreq = freq[c]
            mxChar = c
    res = ""
    if mxChar == "R":
        res = "P"
    elif mxChar == "P":
        res = "S"
    elif mxChar == "S":
        res = "R"
    for _ in range(len(s)):
        print(res, end="")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
