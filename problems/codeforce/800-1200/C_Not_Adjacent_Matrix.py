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
        print(1)
    elif n == 2:
        print(-1)
    else:
        res = [[0 for _ in range(n)] for _ in range(n)]
        c = 1
        for i in range(n):
            res[i][i] = c
            c += 1
        for i in range(1, n):
            for j in range(i):
                res[i][j] = c
                res[j][i] = c+1
                c += 2
        for i in range(n):
            print(*res[i])


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
