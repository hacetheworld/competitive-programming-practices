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


def Solution(arr, n):
    # Write Your Code Here
    sm = sum(arr)
    arr = sorted(arr)
    mx = arr[-1]
    sm = sm-mx
    f = -1
    for i in range(n+1):
        if sm-arr[i] == mx:
            f = i
            break
    if f != -1:
        for i in range(n+1):
            if i != f:
                print(arr[i], end=" ")
        print()
    else:
        sm = sum(arr)-(arr[n]+arr[n+1])
        if sm == arr[n]:
            for i in range(n):
                print(arr[i], end=" ")
            print()
        else:
            print(-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
