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
    isSorted = True
    diff = 0
    if n >= 2:
        diff = arr[1]-arr[0]
    for i in range(1, n):
        if diff != (arr[i] - arr[i-1]):
            isSorted = False
            break

    if n == 1 or n == 2 or isSorted:
        print(0)
        return
    c = 0
    m = 0
    for i in range(1, n-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            c = arr[i+1]-arr[i]
            m = c+arr[i-1]-arr[i]
            break
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            c = arr[i]-arr[i-1]
            m = arr[i]+c-arr[i+1]
            break
    flag = True
    if m != 0:
        for i in range(1, n):
            if arr[i] != (arr[i-1]+c) % m:
                flag = False
                break
    if arr[0] >= m:
        flag = False
    if not flag or m == 0:
        print(-1)
    else:
        print(m, c)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
