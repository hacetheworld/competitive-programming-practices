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
    hash = {}
    res = []
    for v in arr:
        if not v in hash:
            res.append(v)
            hash[v] = True

    for u in res:
        print(u, end=" ")
    print()


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        arr = get_ints_in_list()
        Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
