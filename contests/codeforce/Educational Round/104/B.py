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


def Solution(n, k):
    k -= 1
    if n % 2 == 0:
        ans = (k % (n))
        return ans+1
    else:
        samePoints = n//2
        return (((k//samePoints)+k) % n)+1


def main():
    # //TAKE INPUT HERE
    res = []
    for _ in range(int(input())):
        n, k = get_ints_in_variables()
        res.append(Solution(n, k))
    print(res)


#  call the main method  pa
if __name__ == "__main__":
    main()
