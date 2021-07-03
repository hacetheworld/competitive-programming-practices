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


def Solution(uArr, sArr, n):
    # Write Your Code Here
    hm = [[] for _ in range(n+1)]
    for i in range(n):
        v = uArr[i]
        st = sArr[i]
        hm[v].append(st)
    for i in range(n+1):
        if len(hm[i]):
            hm[i] = sorted(hm[i], reverse=True)
    dp = [[] for _ in range(n+1)]
    for i in range(n+1):
        if(len(hm[i])):
            dp[i].append(hm[i][0])
            for j in range(1, len(hm[i])):
                dp[i].append(dp[i][-1] + hm[i][j])
    ans = [0 for _ in range(n)]
    for k in range(1, n+1):
        if len(hm[k]):
            for i in range(1, len(hm[k])+1):
                ans[i-1] += dp[k][((len(hm[k])//i)*i)-1]
    print(*ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        arr2 = get_ints_in_list()
        Solution(arr, arr2, n)


# calling main Function
if __name__ == '__main__':
    main()
