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


def Solution(n, k):
    # Write Your Code Here
    res = ["a"]
    hm = {}
    a = 0
    for i in range(n-1):
        for j in range(a, k):
            c = chr(97+j)
            pr = res[-1]+c
            if pr in hm:
                continue
            hm[pr] = True
            res.append(c)
            if j == k-1:

                a += 1
            break
    i = 0
    while len(res) < n:
        res.append(res[i % n])
        i += 1
    print("".join(res))


def main():
    # Take input Here and Call solution function
    # for _ in range(get_int()):
    n, k = get_ints_in_variables()
    Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()
