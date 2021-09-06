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


def Solution(s):
    # Write Your Code Here
    aIndex = -1
    for i in range(len(s)):
        if s[i] == "a":
            aIndex = i
    if aIndex == -1:
        print("NO")
        return
    if len(s) == 2 and ("ab" in s or "ba" in s):
        print("YES")
        return

    l = aIndex-1
    r = aIndex+1
    nextChar = "b"
    flag = True
    while l >= 0 and r < len(s):
        if s[l] == nextChar:
            l -= 1
            nextChar = chr(ord(nextChar)+1)
        elif s[r] == nextChar:
            r += 1
            nextChar = chr(ord(nextChar)+1)
        else:
            flag = False
            break
    while flag and l >= 0:
        if s[l] == nextChar:
            l -= 1
            nextChar = chr(ord(nextChar)+1)
        else:
            flag = False
            break
    while flag and r < len(s):
        if s[r] == nextChar:
            r += 1
            nextChar = chr(ord(nextChar)+1)
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
