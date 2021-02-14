# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def Solution(n):
    if n % 2 == 1:
        print("YES")
        return
    while n % 2 == 0:
        n = n//2
    if n == 1:
        print("NO")
    else:
        print("YES")


def main():
    # //TAKE INPUT HERE
    for _ in range(int(stdin.readline())):
        n = int(input())
        # arr = get_ints_in_list()
        # FIND ANSWER HERE
        Solution(n)
        # PRINT OUTPUT HERE


# call the main method
if __name__ == "__main__":
    main()
