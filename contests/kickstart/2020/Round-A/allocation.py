



# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

import sys
import math
from sys import stdin, stdout


# TAKE INPUT

def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def Solution(arr, Budget):
    # Solution
    arr = sorted(arr)
    count = 0
    for h in arr:
        if Budget-h >= 0:
            Budget = Budget-h
            count += 1
    return count


def main():
    # //Write Your Code Here
    for t in range(get_int()):
        N, B = get_ints_in_variables()
        arr = get_ints_in_list()
        print("Case #{}: {}".format(t+1, Solution(arr, B)))


# for printing format
# print("Case #{}: {}".format(t+1, ans))
#  calling main Function
if __name__ == "__main__":
    main()
