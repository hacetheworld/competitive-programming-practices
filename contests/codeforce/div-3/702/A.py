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


def Solution(arr, n):
    count = 0
    for i in range(n-1):
        mn = min(arr[i], arr[i+1])
        mx = max(arr[i], arr[i+1])
        if math.ceil(mx/mn) > 2:
            tmp = mn
            while math.ceil(mx/tmp) > 2:
                count += 1
                tmp *= 2
    print(count)
    # return count


def main():
    # //TAKE INPUT HERE
    op = []
    for _ in range(int(input())):
        n = int(input())
        arr = get_ints_in_list()

        Solution(arr, n)
    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()
