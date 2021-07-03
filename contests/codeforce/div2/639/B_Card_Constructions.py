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


def Solution(t):
    # Write Your Code Here
    ans = 0
    tmp = 1
    for i in range(1, 33):
        tmp = 3*((i*i)//2)+(i//2)
        if tmp >= t:
            ans = i
            break

    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        t = get_int()
        Solution(t)


# calling main Function
if __name__ == '__main__':
    main()
