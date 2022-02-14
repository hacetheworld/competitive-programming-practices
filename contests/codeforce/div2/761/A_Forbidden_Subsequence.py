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


def Solution(s, t):
    # Write Your Code Here
    s = sorted(s)
    for c in "abc":
        if not c in s:
            print("".join(s))
            return
    i = 0
    j = 0
    f = 0
    while i < len(s):
        if s[i] == t[j]:
            j += 1
        i += 1
        if j == 3:
            f = 1
            break
    if f:
        tmp = [c for c in s]
        bsc = 0
        ac = 0
        cc = 0
        for i in range(len(s)):
            c = s[i]
            if c == "a":
                ac += 1
            elif c == "c":
                cc += 1
            elif c == "b":
                bsc += 1
        # print(ac, bsc, cc)
        for i in range(len(s)):
            if ac > 0:
                tmp[i] = "a"
                ac -= 1
            elif cc > 0:
                tmp[i] = "c"
                cc -= 1
            elif bsc > 0:
                tmp[i] = "b"
                bsc -= 1
            else:
                tmp[i] = s[i]
        s = [c for c in tmp]
    print("".join(s))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s = get_string()
        t = get_string()
        Solution(s, t)


# calling main Function
if __name__ == '__main__':
    main()
