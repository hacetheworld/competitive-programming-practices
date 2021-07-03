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


def Solution(arr, n):
    # Write Your Code Here
    s = set()
    for v in arr:
        s.add(v)
    if len(s) == 1:
        print("NO")
        return
    hm = {}
    f = arr[0]
    idx = 1
    s = -1
    for i in range(n):
        v = arr[i]
        if v in hm:
            hm[v].append(i+1)
        else:
            hm[v] = [i+1]
        if v != f:
            s = i+1
    print("YES")
    for v in hm:
        if v == f:
            continue
        for el in hm[v]:
            print(idx, el)
    counter = 0
    for el in hm[f]:
        if counter == 0:
            counter += 1
            continue
        print(s, el)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
