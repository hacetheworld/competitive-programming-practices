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
    for _ in range(int(input())):
        n, k = get_ints_in_variables()
        if n <= k:
            print(math.ceil(k/n))
        else:
            if n % k == 0:
                print(1)
            else:
                print(2)


# call the main method  pa
if __name__ == "__main__":
    main()
