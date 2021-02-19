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
    i = n-1
    while i > 0 and arr[i] <= arr[i-1]:
        i -= 1
    if i <= 0:
        print(0)
        return
    while i > 0 and arr[i] >= arr[i-1]:
        i -= 1
    if i <= 0:
        print(0)
    else:
        print(i)



def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        arr = get_ints_in_list()
        Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
