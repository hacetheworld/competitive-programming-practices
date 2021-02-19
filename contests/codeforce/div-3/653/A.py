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


def Solution(x, y, n):
    rem = n % x
    if rem == y:
        print(n)
        return
    else:
        print(abs(n-(y+rem)))



def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        x, y, n = get_ints_in_variables()
        Solution(x, y, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
