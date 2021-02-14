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


def Solution(s):
    s = [c for c in s]
    i = 0
    while i < len(s):
        if s[i] == "a":
            s[i] = "b"
        else:
            s[i] = "a"
        i += 1
        if i < len(s):
            if s[i] == "z":
                s[i] = "y"
            else:
                s[i] = "z"
        i += 1

    return "".join(s)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        s = get_string()
        print(Solution(s))


#  call the main method  pa
if __name__ == "__main__":
    main()
