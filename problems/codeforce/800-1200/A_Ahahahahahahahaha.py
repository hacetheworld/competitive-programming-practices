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


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        s = sum(arr)
        k = n//2
        if s < k or (k == s and s % 2 == 1):
            tmp = n//2
            print(tmp)
            for _ in range(tmp):
                print(0, end=" ")
            print()
        elif s > k or (s == k and s % 2 == 0):
            tmp = s if s % 2 == 0 else s-1
            print(tmp)
            for _ in range(tmp):
                print(1, end=" ")
            print()


# calling main Function
if __name__ == '__main__':
    main()
