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


def bst(arr, key):
    i = 0
    j = len(arr)-1
    ans = float("inf")
    while i <= j:
        md = (i+j)//2
        if arr[md] >= key:
            j = md-1
            ans = arr[md]
        else:
            i = md+1
    return ans


def Solution():
    # Write Your Code Here
    s1 = get_string()
    s2 = get_string()

    # # print(f)
    frq = {}
    for i in range(len(s1)):
        c = s1[i]
        if c in frq:
            frq[c].append(i)
        else:
            frq[c] = [i]
    # print(frq)
    for c in s2:
        if not c in frq:
            print(-1)
            return
    ans = 1
    i = -1
    for ch in s2:
        i = bisect.bisect_left(frq[ch], i)
        if i >= len(frq[ch]):
            ans += 1
            i = 0
        i = frq[ch][i]+1
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
