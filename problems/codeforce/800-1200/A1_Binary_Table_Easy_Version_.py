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


def Solution(arr, n, m):
    # Write Your Code Here
    res = []
    for i in range(n-1):
        for j in range(1, m-1):
            tmp = []

            if arr[i][j] == 0:
                arr[i][j+1] = 1-arr[i][j+1]
                arr[i+1][j+1] = 1-arr[i][j+1]
                arr[i+1][j] = 1-arr[i][j+1]
                tmp.append(i+1, j+2)
                tmp.append(i+2, j+2)
                tmp.append(i+2, j+1)
            else:
                arr[i][j] = 1-arr[i][j+1]
                arr[i][j+1] = 1-arr[i][j+1]
                arr[i+1][j+1] = 1-arr[i][j+1]
                tmp.append(i+1, j+1)
                tmp.append(i+1, j+2)
                tmp.append(i+2, j+2)
            if j == m-1 and arr[i][j+1] == 1:
                arr[i][j+1] = 1-arr[i][j+1]
                arr[i+1][j] = 1-arr[i][j+1]
                arr[i+1][j+1] = 1-arr[i][j+1]
                tmp.append(i+1, j+2)
                tmp.append(i+2, j+2)
                tmp.append(i+2, j+1)
    for i in range(n-1, n):
        for j in range(1, m-1):
            if arr[i][j] == 0:
                continue
            tmp = []
            if j == 1 and arr[i][j-1] == 1:
                arr[i][j] = 1-arr[i][j+1]
                arr[i][j] = 1-arr[i][j+1]
                arr[i+1][j] = 1-arr[i][j+1]
                tmp.append(i+1, j+2)
                tmp.append(i+1, j+1)
                tmp.append(i+2, j+1)
                arr[i][j+1] = 1-arr[i][j+1]
                arr[i][j] = 1-arr[i][j+1]
                arr[i+1][j+1] = 1-arr[i][j+1]
                tmp.append(i+1, j+2)
                tmp.append(i+1, j+1)
                tmp.append(i+2, j+2)
            if arr[i][j] == 1:
                arr[i][j+1] = 1-arr[i][j+1]
                arr[i+1][j+1] = 1-arr[i][j+1]
                arr[i+1][j-1] = 1-arr[i][j+1]
                tmp.append(i+1, j+2)
                tmp.append(i+1, j+1)
                tmp.append(i+2, j+1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        arr = get_list_of_list(n)
        Solution(arr, n, m)


# calling main Function
if __name__ == '__main__':
    main()
