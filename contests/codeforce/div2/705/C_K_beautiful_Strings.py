from sys import stdin, stdout
from bisect import bisect_right
import heapq
import bisect
import math
import sys
# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

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


def Solution(s, n, k):
    # Write Your Code Here
    if n % k != 0:
        print(-1)
        return
    if k == 1:
        print(s)
        return


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        Solution(s, n, k)


# calling main Function
if __name__ == '__main__':
    main()
