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
    q = get_int()
    mx = {}
    cnt2 = 0
    cnt4 = 0
    cnt6 = 0
    cnt8 = 0
    for v in arr:
        if v in mx:
            mx[v] += 1
            if mx[v] == 2:
                cnt2 += 1
            if mx[v] == 4:
                cnt4 += 1
            if mx[v] == 6:
                cnt6 += 1
            if mx[v] == 8:
                cnt8 += 1
        else:
            mx[v] = 1
    while q:
        s = get_string().split(" ")
        sign = s[0]
        v = int(s[1])
        if sign == "-":
            mx[v] -= 1
            if mx[v] == 1:
                cnt2 -= 1
            if mx[v] == 3:
                cnt4 -= 1
            if mx[v] == 5:
                cnt6 -= 1
            if mx[v] == 7:
                cnt8 -= 1
        else:
            if v in mx:
                mx[v] += 1
                if mx[v] == 2:
                    cnt2 += 1
                if mx[v] == 4:
                    cnt4 += 1
                if mx[v] == 6:
                    cnt6 += 1
                if mx[v] == 8:
                    cnt8 += 1
            else:
                mx[v] = 1
        if cnt4 >= 2 or cnt8 >= 1:
            print("YES")
        elif cnt4 == 0:
            print("NO")
        elif cnt6 >= 1 and cnt2 >= 2 or cnt2 >= 3:
            print("YES")
        else:
            print("NO")
        q -= 1


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
