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


def Solution(arr, n):
    # Write Your Code Here
    mn = float("inf")
    pos = -1
    for i in range(n):
        if arr[i] < mn:
            mn = arr[i]
            pos = i
    st = 0
    ops = -1
    if pos % 2 == 0:
        st = 1
        ops = n//2
    else:
        st = 0
        ops = (n+1)//2
    print(ops)
    r = pow(10, 9)+7
    for i in range(ops):
        print(pos+1, st+1, arr[pos], r)
        st += 2


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
