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


def isPerfectCube(n):
    l = 1
    r = n
    while l <= r:
        mid = (l+r)//2
        tmp = mid*mid*mid
        if tmp == n:
            return True
        elif tmp > n:
            r = mid-1
        else:
            l = mid+1
    return False


def Solution(n):
    for a in range(1, 10000):
        b = n - pow(a, 3)
        if b < 0:
            break
        if isPerfectCube(b):
            print("YES")
            return

    print("NO")


def main():
    # //TAKE INPUT HERE
    op = []
    for _ in range(int(input())):
        n = int(input())
        Solution(n)
    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()
