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


def Solution(arr, n, k):
    # Write Your Code Here
    mod = 998244353
    kFriends = {}
    tmp = sorted(arr.copy())
    for i in range(n-1, (n-k)-1, -1):
        kFriends[tmp[i]] = True
    idxs = []
    for i in range(n):
        if arr[i] in kFriends:
            idxs.append(i+1)
    ans = 1
    for i in range(1, len(idxs)):
        ans = ((ans % mod)*((idxs[i]-idxs[i-1]))) % mod
    s = 0
    for key in kFriends:
        s += key
    print(s, ans)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
