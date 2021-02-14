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


def Solution(n, x):
    n = n % 6
    pos = []
    for p in range(3):
        if p == x:
            pos.append("x")
        else:
            pos.append("-")
    for i in range(n, 0, -1):
        if i % 2 == 0:
            tmp = pos[1]
            pos[1] = pos[2]
            pos[2] = tmp
        else:
            tmp = pos[1]
            pos[1] = pos[0]
            pos[0] = tmp
    for pj in range(3):
        if pos[pj] == "x":
            print(pj)
            return


def main():
    # //TAKE INPUT HERE
    n = int(input())
    x = int(input())
    Solution(n, x)


#  call the main method  pa
if __name__ == "__main__":
    main()
