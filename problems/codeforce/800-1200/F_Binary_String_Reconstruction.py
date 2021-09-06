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


def Solution(a, b, c):
    # Write Your Code Here
    res = []
    if c > 0:
        res.append("1")
    for _ in range(c):
        res.append("1")
    if a > 0:
        res.insert(0, "0")
    for _ in range(a):
        res.insert(0, "0")
    f = 1
    if a > 0 and c > 0:
        f = 0
        b -= 1
    turn = 1 if f and len(res) > 0 and res[-1] == "0" else 0
    for _ in range(b):
        if turn:
            res.append("1")
            turn = 0
        else:
            turn = 1
            res.append("0")
    if a == 0 and c == 0:
        if res[-1] == "1":
            res.append("0")
        else:
            res.append("1")
    print("".join(res))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, b, c = get_ints_in_variables()
        Solution(a, b, c)


# calling main Function
if __name__ == '__main__':
    main()
