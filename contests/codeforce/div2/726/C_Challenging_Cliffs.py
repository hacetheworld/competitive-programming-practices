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
    arr = sorted(arr)
    a = arr[0]
    b = arr[1]
    j = 1
    diff = float("inf")
    for i in range(1, n):
        if arr[i] - arr[i-1] < diff:
            a = arr[i-1]
            b = arr[i]
            j = i
            diff = arr[i] - arr[i-1]
    res = []
    for i in range(j+1, n):
        res.append(arr[i])
    for i in range(j-1):
        res.append(arr[i])
    res.insert(0, a)
    res.append(b)
    print(*res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
