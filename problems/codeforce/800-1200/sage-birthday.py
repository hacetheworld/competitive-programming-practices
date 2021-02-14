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
    ans = 0
    i = 0
    while i < n-1:
        tmp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = tmp
        i += 2
    for i in range(1, n-1):
        if arr[i] < min(arr[i-1], arr[i+1]):
            ans += 1
    print(ans)
    for v in arr:
        print(v, end=" ")
    print()


def main():
    # //TAKE INPUT HERE
    n = int(input())
    arr = get_ints_in_list()
    Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
