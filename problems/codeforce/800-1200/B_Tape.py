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


def Solution(arr, n, m, k):
    # Write Your Code Here
    if k == 1:
        print((arr[-1]-arr[0])+1)
        return
    segs = []
    heap = []
    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        if len(heap) == k-1 and heap[0][0] < diff:
            heapq.heappop(heap)
            heapq.heappush(heap, (diff, i))
        elif len(heap) != k-1:
            heapq.heappush(heap, (diff, i))
    while len(heap):
        segs.append(heapq.heappop(heap)[1])
    segs = sorted(segs)
    prev = 0
    ans = 0
    for i in range(len(segs)):
        ans += (arr[segs[i]]-arr[prev]+1)
        prev = segs[i]+1
    if segs[-1] != n-1:
        ans += arr[-1]-arr[prev]+1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, m, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, m, k)


# calling main Function
if __name__ == '__main__':
    main()
