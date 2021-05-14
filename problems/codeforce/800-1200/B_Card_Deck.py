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

    res = [arr[0]]
    for i in range(1, n):
        res.append(max(res[-1], arr[i]))
    hm = {}
    hm[arr[0]] = 0
    for i in range(n-2, -1, -1):
        if res[i] != res[i+1]:
            hm[res[i+1]] = i+1
    bar = n
    for i in range(len(res)-1, -1, -1):
        for j in range(hm[res[i]], bar):
            print(arr[j], end=" ")
        bar = hm[res[i]]
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
