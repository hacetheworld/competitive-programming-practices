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


def Solution(intial_color, desired_color, painetrs_color, n, m):
    pass



def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n, m = get_ints_in_variables()
        intial_color = get_ints_in_list()
        desired_color = get_ints_in_list()
        painetrs_color = get_ints_in_list()
        Solution(intial_color, desired_color, painetrs_color, n, m)


#  call the main method  pa
if __name__ == "__main__":
    main()
