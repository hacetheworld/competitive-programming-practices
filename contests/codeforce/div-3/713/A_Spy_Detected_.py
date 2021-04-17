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
    hm = {}
    el1 = arr[0]
    el2 = arr[0]
    flag = True
    for i in range(n):
        if flag and el2 != arr[i]:
            el2 = arr[i]
            flag = False
        if arr[i] in hm:
            hm[arr[i]][0] += 1
        else:
            hm[arr[i]] = [1, i+1]
    if hm[el1][0] == 1:
        print(hm[el1][1])
    else:
        print(hm[el2][1])


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
