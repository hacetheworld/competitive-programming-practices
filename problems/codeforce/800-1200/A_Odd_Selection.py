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


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, x = get_ints_in_variables()
        arr = get_ints_in_list()
        oddCount = 0
        evenCount = 0
        for v in arr:
            if v % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        flag = True
        if x % 2 == 0:
            if oddCount % 2 == 0:
                if oddCount > 0 and evenCount > 0 and ((oddCount-1)+evenCount >= x):
                    flag = True
                else:
                    flag = False
            else:
                if oddCount > 0 and evenCount > 0 and ((oddCount)+evenCount >= x):
                    flag = True
                else:
                    flag = False
        else:
            if oddCount % 2 == 0:
                if oddCount > 0 and ((oddCount-1)+evenCount >= x):
                    flag = True
                else:
                    flag = False
            else:
                flag = True
        if flag:
            print("YES")
        else:
            print("NO")


# calling main Function
if __name__ == '__main__':
    main()
