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
    prince = [False for _ in range(n+1)]
    leftGirl = 0
    for i in range(n):
        flag = False
        for j in range(1, len(arr[i])):
            p = arr[i][j]
            if flag:
                continue
            if prince[p]:
                continue
            flag = True
            prince[p] = True
        if not flag:
            leftGirl = i+1
    if leftGirl == 0:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        print(leftGirl, end=" ")
        for p in range(1, n+1):
            if not prince[p]:
                print(p)
                break


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_list_of_list(n)
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
