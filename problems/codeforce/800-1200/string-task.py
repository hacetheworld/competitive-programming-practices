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


def Solution(s):
    s = string_to_list(s)
    for i in range(len(s)):
        c = s[i]
        if c in "AEIOUYyaeiou":
            s[i] = "*"
        else:
            s[i] = "."+c.lower()
    for c in s:
        if c != "*":
            print(c, end="")
    print("")


def main():
    # //TAKE INPUT HERE
    s = get_string()
    Solution(s)


#  call the main method  pa
if __name__ == "__main__":
    main()
