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
    print("2")
    a = n
    b = n-1
    for i in range(n-1):
        print(a, b)
        a = (a+b+1)//2
        b -= 1


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        Solution(n)


#  call the main method  pa
if __name__ == "__main__":
    main()
