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
    A = [[0 for _ in range(n)] for _ in range(n)]
    B = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = arr[i][j]
                B[i][j] = 0
            else:
                s = (arr[i][j]+arr[j][i])/2
                diff = arr[i][j]-s
                A[i][j] = s
                A[j][i] = s
                B[i][j] = diff
                B[j][i] = -diff if diff >= 0 else abs(diff)
    for itm in A:
        print(*itm)
    for itm in B:
        print(*itm)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_list_of_list(n)
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
