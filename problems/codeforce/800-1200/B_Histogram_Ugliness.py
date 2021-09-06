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
    ugliness = arr[0]
    for i in range(1, n):
        ugliness += (abs(arr[i]-arr[i-1]))
    ugliness += arr[-1]
    for i in range(1, n-1):
        if (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            tmp = abs(arr[i]-max(arr[i-1], arr[i+1]))
            ugliness -= tmp
            arr[i] = max(arr[i-1], arr[i+1])
    if n > 1:
        if arr[0] > arr[1]:
            ugliness -= abs(arr[0]-arr[1])
        if arr[-1] > arr[n-2]:
            ugliness -= abs(arr[-1]-arr[n-2])
    else:
        ugliness = arr[0]
    print(ugliness)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
