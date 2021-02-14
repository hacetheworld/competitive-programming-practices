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


def get_signle_int(): return int(input())


def Solution(s):
    stk = []
    for c in s:
        if c == "{":
            stk.append(c)
        else:
            if len(stk) > 0 and stk[-1] == "{":
                stk.pop()
            else:
                stk.append(c)
    s1 = 0
    s2 = 0
    for k in stk:
        if k == "{":
            s1 += 1
        else:
            s2 += 1
    if (s1 & s2 & s1) % 2:
        return(math.ceil((s1+s2)/2))+1
    else:
        return(math.ceil((s1+s2)/2))


def main():
    # //TAKE INPUT HERE
    s = input().strip()
    t = 1
    while not "-" in s:
        print("{}. {}".format(t, Solution(s)))
        t += 1
        s = input().strip()


#  call the main method  pa
if __name__ == "__main__":
    main()
