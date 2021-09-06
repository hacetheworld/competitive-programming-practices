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
        input()
        arr = get_list_of_list(3)
        ans = abs(arr[0][0]-arr[1][0])+abs(arr[0][1]-arr[1][1])
        if (arr[2][0] == arr[0][0] and arr[2][0] == arr[1][0]) and (arr[2][1] >= min(arr[0][1], arr[1][1]) and arr[2][1] < max(arr[0][1], arr[1][1])) or (arr[2][1] == arr[0][1] and arr[2][1] == arr[1][1]) and (arr[2][0] >= min(arr[0][0], arr[1][0]) and arr[2][0] < max(arr[0][0], arr[1][0])):
            ans += 2
        print(ans)


# calling main Function
if __name__ == '__main__':
    main()
