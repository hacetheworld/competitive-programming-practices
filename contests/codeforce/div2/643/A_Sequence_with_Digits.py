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


def minDigit(n):
    ans = 9
    while n:
        if ans > n % 10:
            ans = n % 10
        n = n//10
    return ans


def maxDigit(n):
    ans = 0
    while n:
        if ans < n % 10:
            ans = n % 10
        n = n//10
    return ans


def Solution(a, k):
    # Write Your Code Here
    if k == 1:
        print(a)
        return
    while True:
        mn = minDigit(a)
        mx = maxDigit(a)
        k -= 1
        if k == 0 or mn == 0 or mx == 0:
            print(a)
            return
        a = a+(mn*mx)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, k = get_ints_in_variables()
        Solution(a, k)


# calling main Function
if __name__ == '__main__':
    main()
