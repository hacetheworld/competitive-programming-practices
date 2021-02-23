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


def Solution(s, n):
    stk = []
    for c in s:
        if c == "(":
            stk.append(c)
        else:
            if len(stk) > 0:
                lst = stk[-1]
                if lst == "(":
                    stk.pop()
                else:
                    stk.append(c)
            else:
                stk.append(c)
    print(len(stk)//2)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        s = get_string()
        Solution(s, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
