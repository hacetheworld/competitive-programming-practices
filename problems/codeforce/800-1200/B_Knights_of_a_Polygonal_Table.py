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


def Solution(td, n, k):
    # Write Your Code Here
    mxHeap = []
    td = sorted(td, key=lambda x: x[0])
    prefix = []
    tmp = 0
    for v in td:
        b = v[1]
        tmpAns = tmp+b
        if len(mxHeap) == k:
            if len(mxHeap) and b > mxHeap[0]:
                t = heapq.heappop(mxHeap)
                heapq.heappush(mxHeap, b)
                tmp -= t
                tmp += b
        elif len(mxHeap) < k:
            tmp += b
            heapq.heappush(mxHeap, b)
        prefix.append([tmpAns, v[2]])

    ans = [0 for _ in range(n)]
    for v in prefix:
        ans[v[1]] = v[0]
    print(*ans)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    a = get_ints_in_list()
    b = get_ints_in_list()
    td = [[a[i], b[i], i] for i in range(n)]
    Solution(td, n, k)


# calling main Function
if __name__ == '__main__':
    main()
