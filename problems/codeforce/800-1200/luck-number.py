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


def Solution(n):
    flag = True
    for v in range(10):
        if v == 4 or v == 7:
            continue
        if str(v) in n:
            flag = False
            break
    if flag:
        print("YES")
        return
    luckyNumbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 777]
    for u in luckyNumbers:
        if int(n) % u == 0:
            print("YES")
            return
    print("NO")


def main():
    # //TAKE INPUT HERE
    n = input()
    Solution(n)


#  call the main method  pa
if __name__ == "__main__":
    main()
