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
    if n == 6:
        print(1)
        return
    count = 0
    if n < 6 and n == 3:
        n = n*2
        count += 1
    elif n < 6 and n != 3:
        print(-1)
        return
    q = n//6
    if q == 1:
        print(1)
        return
    while n % 6 == 0:
        n = n*2
        q = n//6
        count += 1
        if q == 6:
            print(count)
            return
    print(-1)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        Solution(n)


#  call the main method  paC

if __name__ == "__main__":
    main()
