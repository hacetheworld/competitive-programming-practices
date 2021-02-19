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


def Solution(a, b):
    x2 = a[2]
    y2 = b[2]
    y1 = b[1]
    r1 = min(x2, y1)

    x2 -= r1
    y1 -= r1
    r2 = 0
    r2 = max(0, y2-x2-a[0])
    res = (2*r1)-(2*r2)
    print(res)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b)


#  call the main method  pa
if __name__ == "__main__":
    main()
