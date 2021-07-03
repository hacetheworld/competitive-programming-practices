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


def Solution(s):
    # Write Your Code Here
    n = len(s)
    i = 1
    j = 0
    prev = []
    bombs = 0
    while i < n:
        if j == - 1 and i < n:
            j = i
            i += 1
        if i == n:
            break
        if s[j]+s[i] == "AB" or s[j]+s[i] == "BB":
            i += 1
            if len(prev) != 0:
                j = prev.pop()
            else:
                j = -1
            bombs += 2
        else:
            i += 1
            prev.append(j)
            j += 1
    print(len(s)-bombs)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
