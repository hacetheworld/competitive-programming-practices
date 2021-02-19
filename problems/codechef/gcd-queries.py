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


def calculatesuffixSuffix(arr, prefix, suffix):
    prefix[1] = arr[0]
    suffix[len(arr)-1] = arr[-1]
    j = len(arr)-2
    for i in range(2, len(arr)):
        prefix[i] = gcd(prefix[i-1], arr[i-1])
    while j >= 0:
        suffix[j] = gcd(suffix[j+1], arr[j])
        j -= 1


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n, q = get_ints_in_variables()
        arr = get_ints_in_list()
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        calculatesuffixSuffix(arr, prefix, suffix)
        for _ in range(q):
            l, r = get_ints_in_variables()
            if l == 1:
                print(suffix[r])
            elif r == len(arr):
                print(prefix[l-1])
            else:
                print(gcd(prefix[l-1], suffix[r]))


#  call the main method  pa
if __name__ == "__main__":
    main()
