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


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def Solution(arr1, arr2, n, m):
    globalGcd = arr1[0]
    for v in arr1:
        globalGcd = gcd(globalGcd, v)
    res = []
    for v in arr2:
        res.append(v+globalGcd)
    for u in res:
        print(u, end=" ")
    print()


def main():
    # //TAKE INPUT HERE
    n, m = get_ints_in_variables()
    arr1 = get_ints_in_list()
    arr2 = get_ints_in_list()
    Solution(arr1, arr2, n, m)


#  call the main method  pa
if __name__ == "__main__":
    main()