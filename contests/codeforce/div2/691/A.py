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


def Solution(redArr, blueArr, n):
    redArr = sorted(redArr)
    blueArr = sorted(blueArr)
    count = 0
    for i in range(n):
        if redArr[i] > blueArr[i]:
            count -= 1
        elif blueArr[i] > redArr[i]:
            count += 1

    if count < 0:
        print("RED")
    elif count > 0:
        print("BLUE")
    else:
        print("EQUAL")


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        redArr = [int(c) for c in get_string()]
        blueArr = [int(c) for c in get_string()]
        Solution(redArr, blueArr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
