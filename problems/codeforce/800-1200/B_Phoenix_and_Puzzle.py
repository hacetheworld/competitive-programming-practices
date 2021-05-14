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


def isPerfectSquare(n):
    flag = False
    i = 1
    while i*i <= n:
        if i*i == n:
            flag = True
            break
        i += 1
    return flag


def Solution():
    # Write Your Code Here
    for _ in range(get_int()):
        n = get_int()
        if n < 5 or n % 2 != 0:
            if n % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            flag = False

            if n % 2 == 0 and isPerfectSquare(n//2):
                flag = True
            if n % 4 == 0 and isPerfectSquare(n//4):
                flag = True
            if flag:
                print("YES")
            else:
                print("NO")


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
