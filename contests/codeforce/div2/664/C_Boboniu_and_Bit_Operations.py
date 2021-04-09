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
    _, _ = get_ints_in_variables()
    a = get_ints_in_list()
    b = get_ints_in_list()
    for ans in range(pow(2, 9)+1):
        isFound = True
        for v in a:
            flag = False
            for u in b:
                if (u & v) | ans == ans:
                    flag = True
                    break
            if not flag:
                isFound = False
                break
        if isFound:
            print(ans)
            break


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
