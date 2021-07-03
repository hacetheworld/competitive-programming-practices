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


def Solution(n):
    # Write Your Code Here
    if n == 1:
        print(4)
    elif n % 2 == 0:
        tmp = (n//2)+1
        print(tmp*tmp)
    else:
        tmp = (n//2)+1
        tmp2 = (n//2)+2
        print(2*tmp*tmp2)


def main():
    # Take input Here and Call solution function
    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
