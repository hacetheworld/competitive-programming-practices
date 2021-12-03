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


def luckyNumbers(n, r, lucky_nums):
    if n > r*10:
        return
    lucky_nums.append(n)
    luckyNumbers((10*n)+4, r, lucky_nums)
    luckyNumbers((10*n)+7, r, lucky_nums)


def helper(n, res):
    ans = 0
    for i in range(1, len(res)):
        ans += (res[i]*(min(res[i], n)-min(res[i-1], n)))
    return ans


def Solution(l, r):
    # Write Your Code Here

    luckyNums = []
    luckyNumbers(0, r, luckyNums)
    luckyNums = sorted(luckyNums)
    # print(luckyNums)
    print(helper(r, luckyNums)-helper(l-1, luckyNums))


def main():
    # Take input Here and Call solution function
    l, r = get_ints_in_variables()
    Solution(l, r)


# calling main Function
if __name__ == '__main__':
    main()
