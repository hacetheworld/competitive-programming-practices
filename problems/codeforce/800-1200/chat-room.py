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
    st = "hello"
    j = 0
    for c in s:
        if j < 5 and c == st[j]:
            j += 1
    if j == 5:
        print("YES")
    else:
        print("NO")


def main():
    # //TAKE INPUT HERE
    s = get_string()
    Solution(s)


#  call the main method  pa
if __name__ == "__main__":
    main()
