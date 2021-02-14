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


def Solution(x, n):
    l = 1
    r = n
    while l <= r:
        mid = (l+r)//2
        if x[mid] == 0:
            print("? ", mid, flush=True)
            x[mid] = int(input())
        if x[mid-1] == 0:
            print("? ", mid-1, flush=True)
            x[mid-1] = int(input())
        if x[mid+1] == 0:
            print("? ", mid+1, flush=True)
            x[mid+1] = int(input())
        if x[mid] < min(x[mid-1], x[mid+1]):
            print("! ", mid, flush=True)
            return
        if (x[mid - 1] < x[mid]):
            r = mid - 1
        else:
            l = mid + 1


def main():
    # //TAKE INPUT HERE
    n = int(input())
    x = [0 for _ in range(n+2)]
    x[0] = float("inf")
    x[n+1] = float("inf")
    stdout.flush()
    Solution(x, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
