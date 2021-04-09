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


def Solution(arr, n, x):
    totalSum = ((x*(x+1))//2)
    tmpSum = 0
    for v in arr:
        if v <= x:
            tmpSum += v
    print(totalSum-(2*tmpSum))


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n, x = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, x)


#  call the main method  pa
if __name__ == "__main__":
    main()
