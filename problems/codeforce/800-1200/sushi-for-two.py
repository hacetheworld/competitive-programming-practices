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
    ans = 0
    i = 0
    while i < n:
        tmpAns = 0
        lel = arr[i]
        counter = 0
        while i < n:
            if arr[i] == lel:
                i += 1
                tmpAns += 1
                counter += 1
            else:
                break
        if i >= n:
            continue
        r = i
        rel = arr[i]
        while counter != 0 and r < n:
            if arr[r] == rel:
                r += 1
                counter -= 1
                tmpAns += 1
            else:
                break
        ans = max(ans, tmpAns-counter)
    print(ans)


def main():
    # //TAKE INPUT HERE
    n = int(input())
    arr = get_ints_in_list()
    Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()
