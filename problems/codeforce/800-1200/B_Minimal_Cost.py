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


def Solution(arr, n, u, v):
    # Write Your Code Here
    s = set()
    for el in arr:
        s.add(el)
    if len(s) == 1:
        print(min([v+v, u+v]))
    else:
        flag = False
        for i in range(1, n):
            if abs(arr[i]-arr[i-1]) >= 2:
                flag = True
                break
        if flag:
            print(0)
        else:
            print(min(u, v))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, u, v = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, u, v)


# calling main Function
if __name__ == '__main__':
    main()
