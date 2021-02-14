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
    if n < 2020:
        print("NO")
        return
    d = n % 10
    n = math.floor(n/10)
    c = n % 10
    n = math.floor(n/10)
    b = n % 10
    n = math.floor(n/10)
    a = n
    if a == c and a % 2 == 0 and b == 0 and d <= c//2:
        print("YES")
    else:
        print("NO")


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
