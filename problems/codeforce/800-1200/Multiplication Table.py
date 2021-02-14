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


def Solution(n, k):
    count = 0
    for i in range(1, n+1):
        if k % i == 0 and i*n >= k:
            count += 1
    print(count)


def main():
    # //TAKE INPUT HERE
    n, k = get_ints_in_variables()
    Solution(n, k)


#  call the main method  pa
if __name__ == "__main__":
    main()
