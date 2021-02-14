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


def string_to_list(s): return [c for c in s]


def get_string(): return sys.stdin.readline().strip()


def main():
    # //TAKE INPUT HERE
    xi = 0
    yi = 0
    zi = 0
    for _ in range(int(input())):
        x, y, z = get_ints_in_variables()
        xi += x
        yi += y
        zi += z
    if xi == 0 and yi == 0 and zi == 0:
        print("YES")
    else:
        print("NO")


#  call the main method  pa
if __name__ == "__main__":
    main()
