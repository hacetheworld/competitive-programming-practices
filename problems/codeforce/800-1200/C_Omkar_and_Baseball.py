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


def check(arr, n):
    for i in range(n+1):
        if arr[i] != i+1:
            return False
    return True


def Solution(arr, n):
    # Write Your Code Here
    i = n-1
    cnt = 0
    idx = -1
    while i >= 0:
        if (i+1) != arr[i]:
            cnt += 1
            if cnt == 2:
                idx = i
                break
            while i >= 0 and (i+1) != arr[i]:
                i -= 1
        i -= 1
    if check(arr, n-1):
        print(0)
    elif idx != -1 and not check(arr, idx):
        print(2)
    else:
        print(1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
