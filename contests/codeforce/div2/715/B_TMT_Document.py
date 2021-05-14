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


def Solution(s, n):
    # Write Your Code Here
    tCount = 0
    mCount = 0
    for c in s:
        if c == "T":
            tCount += 1
    mCount = n-tCount
    if tCount != (2*mCount):
        print("NO")
        return
    counter = 0
    flag = 1
    for i in range(n):
        if s[i] == "T":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            flag = 0
            break

    if not flag:
        print("NO")
        return
    counter = 0
    for i in range(n-1, -1, -1):
        if s[i] == "T":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()
