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


def reverseIt(arr, l, r):
    while l < r:
        tmp = arr[l]
        arr[l] = arr[r]
        arr[r] = tmp
        l += 1
        r -= 1


def findMinIdx(arr, i):
    mx = float("inf")
    id = -1
    for j in range(i, len(arr)):
        if mx > arr[j]:
            mx = arr[j]
            id = j+1
    return id


def Solution(arr, n):
    # Write Your Code Here
    ans = 0
    for i in range(n-1):
        mnIdx = findMinIdx(arr, i)
        ans = ans+(mnIdx-(i+1)+1)
        reverseIt(arr, i, mnIdx-1)
    return ans


def main():
    # Take input Here and Call solution function
    for t in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        print("Case #{}: {}".format(t+1, Solution(arr, n)))


# calling main Function
if __name__ == '__main__':
    main()
