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


def Solution(s, n, p):
    # Write Your Code Here
    s = [cc for cc in s]
    ans = 0
    for i in range(n//2):
        tmp = [s[i], s[n-i-1]]
        tmp = sorted(tmp)
        c1 = tmp[1]
        c2 = tmp[0]
        t = abs((ord(c1)-97)-(ord(c2)-97))
        t2 = abs((ord(c1)-97)-(ord("z")-97)) + \
            abs((ord("a")-97)-(ord(c2)-97))
        t2 += 1
        ans += min(t, t2)
    mid = n//2
    if p >= mid:
        p = n-p+1
    st = 0
    p -= 1
    en = mid-1 if n % 2 == 0 else mid
    while st <= p and s[st] == s[n-st-1]:
        st += 1
    while en >= p and s[en] == s[n-en-1]:
        en -= 1
    if st >= en:
        print(ans)
    else:
        # print(st, en, "st,en,", p,)
        ans += (min(abs(p-en), abs(st-p)))
        ans += abs(en-st)
        print(ans)


def main():
    # Take input Here and Call solution function
    n, p = get_ints_in_variables()
    s = get_string()
    Solution(s, n, p)


# calling main Function
if __name__ == '__main__':
    main()
