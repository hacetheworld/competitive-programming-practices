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


def check(a, h, m, hh, mm):
    hh = int(hh)
    mm = int(mm)
    if (a[hh // 10] == -1 or a[hh % 10] == -1 or a[mm // 10] == -1 or a[mm % 10] == -1):
        return False
    ih = (a[mm % 10] * 10) + a[mm // 10]
    im = (a[hh % 10] * 10) + a[hh // 10]
    return ih < h and im < m


def Solution(s, h, m):
    # Write Your Code Here
    hh = s[:2]
    mm = s[3:]
    a = [0, 1, 5, -1, -1, 2, -1, -1, 8, -1]
    while hh != 0 or mm != 0:
        if check(a, h, m, hh, mm):
            break
        if int(mm) == m-1:
            c = (int(hh)+1) % h
            hh = "0"+str(c) if c < 10 else str(c)
        k = (int(mm)+1) % m
        mm = "0"+str(k) if k < 10 else str(k)
    print(str(int(hh)//10)+str(int(hh) % 10) +
          ":"+str(int(mm)//10)+str(int(mm) % 10))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        h, m = get_ints_in_variables()
        s = get_string()
        Solution(s, h, m)


# calling main Function
if __name__ == '__main__':
    main()
