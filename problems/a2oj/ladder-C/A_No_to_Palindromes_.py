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


def check(s, i, p):
    ch = chr(ord(s[i])+1)
    while ord(ch) < (97+p):
        if i >= 2:
            if s[i-1] != ch and s[i-2] != ch:
                return ch
        elif i >= 1:
            if s[i-1] != ch:
                return ch
        elif i == 0:
            return ch
        ch = chr(ord(ch)+1)
    return None


def Solution(s, n, p):
    # Write Your Code Here
    if p == 1 and n != 1:
        print("NO")
        return
    s = [c for c in s]
    flg = False
    for i in range(n-1, -1, -1):
        t = check(s, i, p)
        if t != None:
            s[i] = t
            flg = True
            break
    for j in range(i+1, n):
        for ch in "abc":
            if j >= 2 and s[j-1] != ch and s[j-2] != ch:
                s[j] = ch
                break
            elif j == 1 and s[j-1] != ch:
                s[j] = ch
                break
    if flg:
        print("".join(s))
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    n, p = get_ints_in_variables()
    s = get_string()
    Solution(s, n, p)


# calling main Function
if __name__ == '__main__':
    main()
