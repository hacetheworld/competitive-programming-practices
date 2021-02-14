# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def Solution(n):
    count = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a+b+c >= 2:
            count += 1
    print(count)


def main():
    # //TAKE INPUT HERE
    n = int(input())
    Solution(n)
    # Broute Force Approach Splution 1
    # count = 0
    # for _ in range(n):
    #     a, b, c = map(int, input().split())
    #     if a+b+c >= 2:
    #         count += 1
    # print(count)


#  call the main method  pa
if __name__ == "__main__":
    main()
