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


def Solution(arr, n, x):
    # Write Your Code Here
    arr = sorted(arr)
    i = n-1
    ans = 0
    # print(arr)
    while i >= 0:
        tmp = arr[i]
        j = 1
        while i > 0 and (tmp*j) < x:
            i -= 1
            j += 1
            if i < 0:
                break
            tmp = arr[i]
        if tmp*j >= x:
            ans += 1
        i -= 1

    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, x = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, x)


# calling main Function
if __name__ == '__main__':
    main()
