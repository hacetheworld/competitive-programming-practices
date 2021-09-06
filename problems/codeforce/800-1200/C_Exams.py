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
    arr = sorted(arr, key=lambda x: x[0])
    day = -1
    j = 0
    while j < n:
        heap = []
        heapq.heappush(heap, arr[j])
        while j < n-1 and arr[j][0] == arr[j+1][0]:
            heapq.heappush(heap, arr[j+1])
            j += 1
        while len(heap):
            itm = heapq.heappop(heap)
            cday = itm[1]
            if cday >= day:
                day = cday
            else:
                day = itm[0]
        j += 1
    print(day)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_list_of_list(n)
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
