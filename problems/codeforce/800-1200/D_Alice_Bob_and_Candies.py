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
    alice = 0
    bob = 0
    move = 0
    i = 0
    j = n-1
    prev = 0
    while i <= j:
        flag = False
        tmp = 0
        while tmp <= prev and i <= j:
            alice += arr[i]
            tmp += arr[i]
            flag = True
            i += 1
        if flag:
            move += 1
        flag = False
        prev = tmp
        tmp = 0
        while tmp <= prev and j >= i:
            bob += arr[j]
            tmp += arr[j]
            flag = True
            j -= 1
        if flag:
            move += 1
        prev = tmp
    print(move, alice, bob)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
