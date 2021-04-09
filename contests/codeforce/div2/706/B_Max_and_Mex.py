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


def Solution(arr, n, k):
    # Write Your Code Here
    mp = {}
    uniq = 0
    mx = max(arr)
    for v in arr:
        if v in mp:
            mp[v] += 1
        else:
            mp[v] = 1
        if mp[v] == 1:
            uniq += 1
    me = float("inf")
    for i in range(mx+1):
        if not i in mp:
            me = i
            break
    if me < mx and k != 0:
        avg = math.ceil((me+mx)/2)
        if avg in mp:
            mp[avg] += 1
        else:
            mp[avg] = 1
        if mp[avg] == 1:
            uniq += 1
    elif me > mx and k != 0:
        uniq += k
    print(uniq)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
