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


def Solution(arr, n, p, k):
    # Write Your Code Here
    arr = sorted(arr)
    sm = 0
    ans = 0
    prefix = 0
    for i in range(k+1):
        sm = prefix
        if sm > p:
            break
        cnt = i
        for j in range(((k+i)-1), n, k):
            if sm+arr[j] <= p:
                cnt += k
                sm += arr[j]
            else:
                break
        if i == n:
            break
        prefix += arr[i]
        ans = max(ans, cnt)
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, p, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, p, k)


# calling main Function
if __name__ == '__main__':
    main()
