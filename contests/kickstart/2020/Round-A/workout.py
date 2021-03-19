# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

import sys
import math
import heapq
from sys import stdin, stdout


# TAKE INPUT

def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def Solution(arr, n, k):
    heap = []
    for i in range(1, n):
        f = arr[i]
        s = arr[i-1]
        heapq.heappush(heap, ((s-f), f, s))
    for _ in range(k):
        mxDiff = heapq.heappop(heap)

        if -1*mxDiff[0] == 1:
            break
        f, s = mxDiff[1], mxDiff[2]
        mid = (f+s)//2
        firestEl = (mid-f, f, mid)
        secondEl = (s-mid, mid, s)
        heapq.heappush(heap, firestEl)
        heapq.heappush(heap, secondEl)
    ans = heapq.heappop(heap)
    return -1*ans[0]


def main():
    # //Write Your Code Here
    for t in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        ans = Solution(arr, n, k)
        print("Case #{}: {}".format(t+1, ans))


# for printing format
# print("Case #{}: {}".format(t+1, ans))
#  calling main Function
if __name__ == "__main__":
    main()
