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


def Solution(arr, n):
    pass


def main():
    # //TAKE INPUT HERE
    n, k = get_ints_in_variables()
    print(3*n+min(n-k, k-1))


#  call the main method  pa
if __name__ == "__main__":
    main()
