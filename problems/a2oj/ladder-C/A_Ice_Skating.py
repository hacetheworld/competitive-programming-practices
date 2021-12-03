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
    queue = []
    comp = 0
    while len(arr) > 0:
        queue.append(arr.pop(0))
        comp += 1
        while len(queue) > 0:
            itm = queue.pop()
            i = 0
            while i < len(arr):
                if arr[i][0] == itm[0] or arr[i][1] == itm[1]:
                    queue.append(arr[i])
                    arr.pop(i)
                else:
                    i += 1
    print(comp-1)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_list_of_list(n)
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
