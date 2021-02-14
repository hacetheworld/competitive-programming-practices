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


def Solution(arr, n, k):
    count = 0
    k = arr[-1] if k == n else arr[k-1]
    for v in arr:
        if v > 0 and v >= k:
            count += 1
    print(count)


def main():
    # //TAKE INPUT HERE
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


#  call the main method  pa
if __name__ == "__main__":
    main()
