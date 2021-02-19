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
    extra = arr[0]
    for i in range(n-1):
        extra = extra-i-1+arr[i+1]
        if extra < 0:
            print("NO")
            return
    print("YES")


def main():
    # //TAKE INPUT HERE
    # op = []
    for _ in range(int(input())):
        n = int(input())
        arr = get_ints_in_list()
        Solution(arr, n)
    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()
