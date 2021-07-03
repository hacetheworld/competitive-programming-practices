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


def Solution(arr, n):
    # Write Your Code Here
    dp = [1 for _ in range(n+1)]
    arr.insert(0, 0)
    for i in range(2, n+1):
        j = 1
        while j*j <= i:
            if((i % j) == 0):
                d1 = j
                d2 = i//j
                if(arr[d1] < arr[i]):
                    dp[i] = max(dp[i], 1+dp[d1])

                if(arr[d2] < arr[i]):
                    dp[i] = max(dp[i], 1+dp[d2])
            j += 1
    print(max(dp))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
