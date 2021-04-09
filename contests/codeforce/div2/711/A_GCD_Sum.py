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


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def Solution(n):
    # Write Your Code Here
    while True:
        counOfDigits = 0
        tmp = n
        while tmp > 0:
            counOfDigits += (tmp % 10)
            tmp = tmp//10
        if gcd(n, counOfDigits) > 1:
            print(n)
            return
        n += 1


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        Solution(n)


# calling main Function
if __name__ == '__main__':
    main()
