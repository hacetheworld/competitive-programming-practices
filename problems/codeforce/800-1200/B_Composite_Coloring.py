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
    if n == 1:
        print(1)
        print(1)
        return
    else:
        res = []
        for v in arr:
            if v % 2 == 0:
                res.append(1)
            elif v % 3 == 0:
                res.append(2)
            elif v % 5 == 0:
                res.append(3)
            elif v % 7 == 0:
                res.append(4)
            elif v % 11 == 0:
                res.append(5)
            elif v % 13 == 0:
                res.append(6)
            elif v % 17 == 0:
                res.append(7)
            elif v % 19 == 0:
                res.append(8)
            elif v % 23 == 0:
                res.append(9)
            elif v % 29 == 0:
                res.append(10)
            elif v % 31 == 0:
                res.append(11)
        hm = {}
        count = 0
        for v in res:
            if v in hm:
                continue
            hm[v] = True
            count += 1
        c = 1
        hm = {}
        for i in range(n):
            if res[i] in hm:
                res[i] = hm[res[i]]
            else:
                hm[res[i]] = c
                res[i] = c
                c += 1
        print(c-1)
        print(*res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
