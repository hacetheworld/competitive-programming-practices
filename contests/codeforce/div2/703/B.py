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


def getTwoDArray(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def Solution(arrx, arry, n):
    if n % 2 == 0:
        id = n//2
        arrx = sorted(arrx)
        x = arrx[id]-arrx[id-1]+1
        arry = sorted(arry)
        y = arry[id]-arry[id-1]+1
        print(x*y)
    else:
        print(1)


def main():
    # //TAKE INPUT HERE
    # op = []
    for _ in range(int(input())):
        n = int(input())
        arrx, arry = [], []
        for _ in range(n):
            x, y = get_ints_in_variables()
            arrx.append(x)
            arry.append(y)
        Solution(arrx, arry, n)

    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()
