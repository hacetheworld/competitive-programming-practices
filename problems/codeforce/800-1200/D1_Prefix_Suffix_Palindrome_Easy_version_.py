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


def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def Solution(s):
    # Write Your Code Here
    n = len(s)
    res = ["" for _ in range(n)]
    i = 0
    j = n-1
    while i < j:
        if s[i] == s[j]:
            res[i] = s[i]
            res[j] = s[j]
        else:
            break
        i += 1
        j -= 1
    f = 1
    if i == j:
        res[i] = s[i]
        f = 0
    if f:
        pf = []
        pftmp = []
        for k in range(i, j+1):
            pf.append(s[k])
            if isPalindrome(pf):
                pftmp = [c for c in pf]
        sf = []
        sftmp = []
        for k in range(j, i-1, -1):
            sf.append(s[k])
            if isPalindrome(sf):
                sftmp = [c for c in sf]
        t = pftmp if len(pftmp) > len(sftmp) else sftmp
        # print(res, t)
        i = 0
        while i < n and res[i] != "":
            i += 1
        # i -= 1
        for j in range(len(t)):
            res[j+i] = t[j]
    for c in res:
        if c != "":
            print(c, end="")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
