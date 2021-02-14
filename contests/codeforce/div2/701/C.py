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


def Solution(a, b):
    res = float("inf")
    counterOfB = 0 if b > 1 else 1
    j = b if b > 1 else b+1
    while True:
        tmp = 0
        t = a
        while t > 0:
            tmp += 1
            t = t//j
        if (tmp+counterOfB) > res:
            break
        res = min(tmp+counterOfB, res)
        counterOfB += 1
        j += 1
    print(res)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        a, b = get_ints_in_variables()
        Solution(a, b)


#  call the main method  pa
if __name__ == "__main__":
    main()
