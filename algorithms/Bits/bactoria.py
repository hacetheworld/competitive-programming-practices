
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


def Solution(x):
    if x == 1:
        print(1)
        return
    tmp = 2
    while tmp <= x:
        if 2*tmp <= x:
            tmp = 2*tmp
        else:
            break
    print(x-tmp)
    print(1+(x-tmp))


def main():
    # //TAKE INPUT HERE
    x = int(input())
    Solution(x)


#  call the main method  pa
if __name__ == "__main__":
    main()
