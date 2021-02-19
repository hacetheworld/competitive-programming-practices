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


def ask(l, r):
    if l == r:
        return -1
    print("?", l, r, flush=True)
    return int(input())


def Solution(n):
    pos = ask(1, n)
    if ask(1, pos) == pos:
        l = 1
        r = pos
        while l < r:
            mid = (l+r+1)//2
            if ask(mid, n) == pos:
                l = mid
            else:
                r = mid-1
        print("!", l)
    else:
        l = pos
        r = n
        while l < r:
            mid = (l+r)//2
            if ask(1, mid) == pos:
                r = mid
            else:
                l = mid+1
        print("!", l)


def main():
    # //TAKE INPUT HERE
    n = int(input())
    Solution(n)


#  call the main method  pa
if __name__ == "__main__":
    main()
