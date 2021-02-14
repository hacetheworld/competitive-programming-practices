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


def TrenarySearch(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        m1 = l+((r-l)//3)
        m2 = r-((r-l)//3)
        if arr[m1] == target:
            return m1
        if arr[m2] == target:
            return m2
        if target < arr[m1]:
            r = m1-1
        if arr[m2] < target:
            l = m2+1
        else:
            l = m1+1
            r = m2-1

    return -1


def main():
    # //TAKE INPUT HERE
    n = int(input())
    arr = get_ints_in_list()
    target = int(input())
    print(TrenarySearch(arr, target))


#  call the main method  pa
if __name__ == "__main__":
    main()
