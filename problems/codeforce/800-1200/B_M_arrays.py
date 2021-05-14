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


def Solution(arr, n, m):
    # Write Your Code Here
    ans = 0
    hm = {}
    for i in range(m):
        hm[i] = 0
    for i in range(n):
        hm[arr[i] % m] += 1

    if hm[0] >= 1:
        ans += 1

    for i in range(1, m):
        if hm[i]:
            if abs(hm[i]-hm[m-i]) <= 1:
                ans += 1
            else:
                ans += abs(hm[i]-hm[m-i])
            hm[m-i] = 0
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, m)


# calling main Function
if __name__ == '__main__':
    main()
