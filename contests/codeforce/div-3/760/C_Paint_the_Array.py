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
    gcdOdd = 0
    gcdEven = 0
    for i in range(n):
        if (i+1) % 2:
            gcdOdd = math.gcd(gcdOdd, arr[i])
        else:
            gcdEven = math.gcd(gcdEven, arr[i])
    f = 1
    for i in range(n):
        if (i+1) % 2 == 0 and arr[i] % gcdOdd == 0:
            f = 0
            break
    if f:
        print(gcdOdd)
        return
    f = 1
    for i in range(n):
        if (i+1) % 2 and arr[i] % gcdEven == 0:
            f = 0
            break
    if f:
        print(gcdEven)
        return
    print(0)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
