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


def Solution(a, n):
    # Write Your Code Here
    hm = {}
    for v in a:
        if v in hm:
            hm[v] += 1
        else:
            hm[v] = 1
    ans = 0
    arr = []
    for v in hm:
        arr.append(hm[v])
    arr = sorted(arr, reverse=True)
    taken = arr[0]
    # print(arr)
    ans = arr[0]
    for i in range(1, len(arr)):
        if taken <= 0:
            break
        if arr[i] >= taken:
            ans += (taken-1)
            taken -= 1
        else:
            ans += arr[i]
            taken = arr[i]
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        Solution(a, n)


# calling main Function
if __name__ == '__main__':
    main()
