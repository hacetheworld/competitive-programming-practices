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


def getPrime():
    p = [1]*1001
    for i in range(2, 1001):
        if p[i]:
            for j in range(i, 1001, i):
                p[j] = 0
            p[i] = 1
    return p


def Solution():
    # Write Your Code Here
    s = get_string()
    n = len(s)
    primes = getPrime()
    cntArr = [0]*26
    for i in range(n):
        cntArr[ord(s[i])-97] += 1
    p = 0
    for i in range((n//2)+1, n+1):
        if primes[i]:
            p += 1
    if max(cntArr) < n-1-p:
        print("NO")
        return
    ans = [""]*(n+1)
    id = cntArr.index(max(cntArr))
    for i in range(2, (n//2)+1):
        ans[i] = chr(97+id)
        cntArr[id] -= 1
    for i in range((n//2)+1, n+1):
        if not primes[i]:
            ans[i] = chr(97+id)
            cntArr[id] -= 1
    j = 0
    for i in range(1, n+1):
        if ans[i] == "":
            while cntArr[j] <= 0:
                j += 1
            ans[i] = chr(97+j)
            cntArr[j] -= 1
    print("YES")
    print("".join(ans[1::]))


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
