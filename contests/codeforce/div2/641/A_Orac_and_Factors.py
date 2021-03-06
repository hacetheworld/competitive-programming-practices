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


def smallestDivisor(n):
    if n <= 3:
        return n
    i = 2
    while i*i <= n:
        if n % i == 0:
            return i
        i += 1
    return n


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        d = smallestDivisor(n)
        ans = n+d
        ans += (2*(k-1))
        print(ans)


# calling main Function
if __name__ == '__main__':
    main()
