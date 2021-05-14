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


def Solution(arr, n, x):
    # Write Your Code Here
    ans = n
    s = sum(arr)
    if (s % x) != 0:
        print(ans)
    else:
        flag = 1
        for v in arr:
            if v % x != 0:
                flag = 0
                break

        if flag:
            print(-1)
            return
        counter = 0
        tmp = s
        for v in arr:
            tmp -= v
            counter += 1
            if tmp % x != 0:
                break
        ans = ans-(counter)
        tmp = s
        counter = 0
        for i in range(n-1, -1, -1):
            v = arr[i]
            tmp -= v
            counter += 1
            if tmp % x != 0:
                break
        ans = max(ans, n-(counter))
        print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, x = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, x)


# calling main Function
if __name__ == '__main__':
    main()
