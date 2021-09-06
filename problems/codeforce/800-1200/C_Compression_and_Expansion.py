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


def Solution(arr, n):
    # Write Your Code Here
    res = []
    for v in arr:
        if v == 1:
            if len(res) and res[-1] != ".":
                res.append(".")
            res.append("1")
            print("".join(res))
        else:
            num = v
            if len(res) and str(v) == res[-1]:
                while len(res) and (int(res[-1])) >= v:
                    res.pop()
                    if len(res):
                        res.pop()
                res.pop()
                if len(res):
                    res.pop()
                num = v
            elif len(res) > 0 and v < int(res[-1]):
                while len(res) and (int(res[-1])) >= v:
                    res.pop()
                    if len(res):
                        res.pop()
                res.pop()
                if len(res):
                    res.pop()
                num = v
            elif len(res) > 0 and v > int(res[-1]):
                while len(res) and (int(res[-1])+1) != v:
                    res.pop()
                    if len(res):
                        res.pop()
                res.pop()
                if len(res):
                    res.pop()
                num = v
            if len(res) and res[-1] != ".":
                res.append(".")
            res.append(str(num))
            print("".join(res))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = [get_int() for _ in range(n)]
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
