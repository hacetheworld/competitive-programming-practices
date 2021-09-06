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

    freq = []
    ans = 0
    for s in arr:
        hm = [0, 0, 0, 0, 0]
        for c in s:
            hm[ord(c)-97] += 1
        freq.append(hm)
    for i in range(5):
        queue = []
        for j in range(n):
            itm = freq[j]
            sm = sum(itm)
            heapq.heappush(queue, -1*(itm[i]-(sm-itm[i])))
        sm = 0
        tmpAns = 0
        while len(queue):
            v = -1*heapq.heappop(queue)
            if sm+v > 0:
                tmpAns += 1
                sm += v
            else:
                break
        ans = max(ans, tmpAns)
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = [get_string() for _ in range(n)]
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
