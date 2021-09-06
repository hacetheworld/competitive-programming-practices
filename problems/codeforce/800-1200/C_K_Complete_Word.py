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


def Solution(s, n, k):
    # Write Your Code Here
    ans = 0
    for i in range(k//2):
        cnt = [0 for _ in range(26)]
        for j in range(0, (n-k)+1, k):
            el = s[j+i]
            el2 = s[j+k-1-i]
            cnt[ord(el)-97] += 1
            cnt[ord(el2)-97] += 1
        totl = 2*(n//k)
        mx = max(cnt)
        ans += (totl-mx)
    if k % 2:
        cnt = [0 for _ in range(26)]
        for j in range(k//2, n, k):
            el = s[j]
            cnt[ord(el)-97] += 1
        totl = (n//k)
        mx = max(cnt)
        ans += (totl-mx)
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        Solution(s, n, k)


# calling main Function
if __name__ == '__main__':
    main()
