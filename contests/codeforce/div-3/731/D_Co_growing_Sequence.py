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


def countBits(p, v):
    # if p == 0 and v == 0:
    #     return 0
    s = []
    while v and p:
        if v % 2 == p % 2:
            s.append("0")
        else:
            s.append("0" if v % 2 else "1")
        v = v//2
        p = p//2
    # while v:
    #     s.append("1")
    #     v = v//2
    # print(p, "p")
    while p:
        s.append(str(p % 2))
        p = p//2
    # print(s)
    if len(s) == 0:
        s = ["0"]
    return int("".join(list(reversed(s))), 2)


def Solution(arr, n):
    # Write Your Code Here
    res = [0]
    for i in range(1, n):
        res.append(countBits((res[-1] ^ arr[i-1]), arr[i]))
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
