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


def BinarySearch(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = l+((r-l)//3)
        if arr[mid] == target:
            return mid
        elif arr[l] == target:
            return l
        elif arr[r] == target:
            return r
        if target < arr[mid] and target > arr[l]:
            r = mid-1
        else:
            l = mid+1

    return -1


def main():
    # //TAKE INPUT HERE
    n = int(input())
    arr = get_ints_in_list()
    target = int(input())
    print(BinarySearch(arr, target))


#  call the main method  pa
if __name__ == "__main__":
    main()
