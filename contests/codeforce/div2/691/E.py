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
    m = float("inf")
    for v in arr1:
        if m > v:
            m = v
    if len(arr1) == 1:
        for b in arr2:
            print(arr1[0]+b, end=" ")
        return
    globalGcd = abs(arr1[1]-arr1[0])
    for i in range(1, len(arr1)):
        globalGcd = gcd(globalGcd, abs(arr1[i]-arr1[i-1]))
    for b in arr2:
        print(gcd(globalGcd, m+b), end=" ")


def main():
    # //TAKE INPUT HERE
    n, m = get_ints_in_variables()
    arr1 = get_ints_in_list()
    arr2 = get_ints_in_list()
    Solution(arr1, arr2, n, m)


#  call the main method  pa
if __name__ == "__main__":
    main()
