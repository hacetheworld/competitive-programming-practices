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


def Solution(arr, n):
    stk = []
    res = []
    for i in range(n-1, -1, -1):
        el = arr[i]
        while len(stk) > 0 and el > stk[-1]:
            stk.pop()
        if len(stk) == 0:
            res.append(-1)
        else:
            res.append(stk[-1])
        stk.append(el)
    return reversed(res)


def main():
    # //TAKE INPUT HERE
    n = get_signle_int()
    arr = get_ints_in_list()
    print(list(Solution(arr, n)))


#  call the main method  pa
if __name__ == "__main__":
    main()
