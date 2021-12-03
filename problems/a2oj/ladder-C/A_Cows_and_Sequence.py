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


def Solution(n):
    # Write Your Code Here
    arr = [0 for _ in range(n+1)]
    sm = 0
    offset = [0 for _ in range(n+1)]
    # lst=-1
    # ttl = 0
    cnt = 1
    for _ in range(n):
        t = get_ints_in_list()
        # print(t, "jjj")
        if len(t) == 3:
            sm += (t[1]*t[2])
            offset[t[1]-1] += t[2]
        elif len(t) == 2:
            sm += t[1]
            arr[cnt] = t[1]
            cnt += 1
        else:
            sm -= offset[cnt-1]
            offset[cnt-2] += offset[cnt-1]
            offset[cnt-1] = 0
            sm -= arr[cnt-1]
            arr[cnt-1] = 0
            cnt -= 1
        print(sm/cnt)


def main():
    # Take input Here and Call solution function

    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()
