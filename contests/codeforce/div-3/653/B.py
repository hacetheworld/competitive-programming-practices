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


def Solution(n):
    if n == 1:
        print(0)
        return
    cnt2 = 0
    cnt3 = 0
    d = 2
    while n > 1:
        if d > 3:
            break
        if n % d == 0:
            n = n//d
            if d == 2:
                cnt2 += 1
            elif d == 3:
                cnt3 += 1
        else:
            d += 1
    if d > 3:
        print(-1)
    elif cnt2 > cnt3:
        print(-1)
    else:
        print((cnt3-cnt2)+cnt3)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        Solution(n)


#  call the main method  paC

if __name__ == "__main__":
    main()
