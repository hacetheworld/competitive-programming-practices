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


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s = get_string()
        n = len(s)
        y = 0
        flag = 0
        for i in range(n-1, 0, -1):
            if s[i-1] == "0" and s[i] == "0":
                y = i
                flag = 1
                break
        if not flag:
            print("YES")
            continue
        if flag:
            for i in range(0, y):
                if s[i+1] == "1" and s[i] == "1":
                    flag = 0
                    break
        if not flag:
            print("NO")
        else:
            print("YES")


# calling main Function
if __name__ == '__main__':
    main()
