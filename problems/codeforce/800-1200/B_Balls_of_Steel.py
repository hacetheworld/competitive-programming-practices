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


def Solution(cord, n, k):
    # Write Your Code Here
    for i in range(n):
        r = 0
        for j in range(n):
            if abs(cord[i][0]-cord[j][0])+abs(cord[i][1]-cord[j][1]) > k:
                break
            r += 1
        if r == n:
            print(1)
            return
    print(-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        cord = [get_ints_in_list() for _ in range(n)]
        Solution(cord, n, k)


# calling main Function
if __name__ == '__main__':
    main()
