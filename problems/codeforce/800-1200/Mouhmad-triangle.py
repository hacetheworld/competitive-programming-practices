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
    arr = sorted(arr)
    flag = False
    for i in range(2, n):
        if arr[i-1]+arr[i-2] > arr[i]:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # //TAKE INPUT HERE
    n = int(input())
    arr = get_ints_in_list()
    Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
