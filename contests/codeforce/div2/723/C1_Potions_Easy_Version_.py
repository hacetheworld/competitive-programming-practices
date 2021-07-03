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


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    mnheap = []
    ans = 0
    potion = 0
    for v in arr:
        if v >= 0:
            ans += 1
            potion += v
        else:
            if potion+v >= 0:
                potion += v
                ans += 1
                heapq.heappush(mnheap, v)
            else:
                if len(mnheap):
                    itm = mnheap[0]
                    if itm < v:
                        heapq.heappop(mnheap)
                        potion += abs(itm)
                        potion += v
                        heapq.heappush(mnheap, v)

    print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
