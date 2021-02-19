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


def getCoast(s, l, r, ch):
    cost = 0
    for c in range(l, r):
        if s[c] == chr(ch):
            continue
        cost += 1
    return cost


def getMin(s, ch, l, r):
    if l == r-1:
        if s[l] == chr(ch):
            return 0
        else:
            return 1
    mid = (l+r)//2
    left = getCoast(s, l, mid, ch)+getMin(s, ch+1, mid, r)
    right = getMin(s, ch+1, l, mid)+getCoast(s, mid, r, ch)

    return min(left, right)


def Solution(s, n):
    print(getMin(s, ord("a"), 0, n))


def main():
    # //TAKE INPUT HERE
    # op = []
    for _ in range(int(input())):
        n = int(input())
        s = get_string()
        Solution(s, n)
    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()
