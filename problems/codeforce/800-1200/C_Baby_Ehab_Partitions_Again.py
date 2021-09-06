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


def helper(arr, i, n, currSum, SumToMake, dp):
    if i >= n:
        return False
    if currSum > SumToMake:
        return False
    if currSum == SumToMake:
        return True
    if dp[i][currSum] != -1:
        return dp[i][currSum]
    dp[i][currSum] = helper(arr, i+1, n, currSum+arr[i], SumToMake,
                            dp) or helper(arr, i+1, n, currSum, SumToMake, dp)
    return dp[i][currSum]


def Solution(arr, n):
    # Write Your Code Here
    s = sum(arr)
    if s % 2:
        print(0)
        return
    dp = [[-1 for _ in range((s//2)+1)] for _ in range(n)]
    res = helper(arr, 0, n, 0, s//2, dp)
    if res:
        print(1)
        ans = -1
        for i in range(n):
            if arr[i] % 2:
                ans = i+1
                break
        if ans == -1:
            while True:
                for i in range(n):
                    if arr[i] % 2 == 0:
                        arr[i] = arr[i]//2
                    else:
                        ans = i+1
                        break
                if ans != -1:
                    break
        print(ans)
    else:
        print(0)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
