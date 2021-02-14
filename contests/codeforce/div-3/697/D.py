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


def Solution(arr, n):
    pass


def main():
    # //TAKE INPUT HERE
    t = int(stdin.readline())
    # print(t)
    for _ in range(t):
        n = get_ints_in_variables()
        arr = get_ints_in_list()
        # FIND ANSWER HERE
        Solution(arr, n)
        # PRINT OUTPUT HERE


# call the main method
if __name__ == "__main__":
    main()
