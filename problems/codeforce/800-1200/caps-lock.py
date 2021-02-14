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
    tmp = s
    s = string_to_list(s)
    sm = 0
    mx = 0
    for i in range(len(s)):
        if s[i] == s[i].lower():
            sm += 1
        else:
            mx += 1

    if mx == len(s):
        print(tmp.lower())
        return
    if len(s) == 1:
        print(tmp.upper())
        return
    if sm == len(s):
        print(tmp)
        return
    if s[0] == s[0].lower() and mx == len(s)-1:
        s = [s[i].lower() if i != 0 else s[i].upper() for i in range(len(s))]
        print("".join(s))
        return
    print(tmp)


def main():
    # //TAKE INPUT HERE
    s = get_string()
    Solution(s)


#  call the main method  pa
if __name__ == "__main__":
    main()
