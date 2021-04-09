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


def Solution(s, n, k):
    # Write Your Code Here
    count = 0
    for c in s:
        if c != ".":
            count += 1
    if count == 1:
        print(1)
    else:
        f, l = 0, n
        i = 0
        while i < n:
            if s[i] != '.':
                f = i
                break
            i += 1
        i = n-1
        while i >= 0:
            if s[i] != '.':
                l = i
                break
            i -= 1
        tmp = 0
        i = f+k
        l = l
        while i < l:
            tmp += 1
            i += k
        print(2+tmp)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        Solution(s, n, k)


# calling main Function
if __name__ == '__main__':
    main()
