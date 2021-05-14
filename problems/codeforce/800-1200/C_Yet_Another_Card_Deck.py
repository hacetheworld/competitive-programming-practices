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


def Solution(arr, queries, n, q):
    # Write Your Code Here
    hm = {}
    for i in range(n):
        if arr[i] in hm:
            continue
        hm[arr[i]] = i+1
    for q in queries:
        print(hm[q], end=" ")
        val = hm[q]
        for v in hm:
            if hm[v] < val:
                hm[v] += 1
        hm[q] = 1

    print()


def main():
    # Take input Here and Call solution function
    n, q = get_ints_in_variables()
    arr = get_ints_in_list()
    queries = get_ints_in_list()

    Solution(arr, queries, n, q)


# calling main Function
if __name__ == '__main__':
    main()
