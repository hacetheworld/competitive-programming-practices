# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
# Codechef  : https://www.codechef.com/users/majay1638
# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def Solution(s):
    stringAlphabet = []
    stringNumbers = []
    stringSpecialChar = []

    for c in s:
        if c in "123456789":
            stringNumbers.append(c)
        elif c in "!@#$%^&*~?><.,-_":
            stringSpecialChar.append(c)
        else:
            stringAlphabet.append(c)
    print("".join(stringAlphabet) if len(stringAlphabet) > 0 else "")
    print("".join(stringNumbers) if len(stringNumbers) > 0 else "")
    print("".join(stringSpecialChar) if len(stringSpecialChar) > 0 else "")


def main():
    # //TAKE INPUT HERE
    # op = []
    for _ in range(int(input())):
        s = get_string()
        Solution(s)
    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()
