# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------------- SOLUTION FUNCTION ------------------


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, b = get_ints_in_variables()
        steps = 0
        mx = max(a, b)
        mn = min(a, b)
        if mx == mn:
            print(steps)
        elif mx % mn == 0:
            flag = 0
            mx = mx//mn
            while mx != 1:
                if mx % 8 == 0:
                    mx = mx//8
                elif mx % 4 == 0:
                    mx = mx//4
                elif mx % 2 == 0:
                    mx = mx//2
                else:
                    flag = 1
                    break
                steps += 1
            if flag:
                print(-1)
            else:
                print(steps)

        else:
            print(-1)


# calling main Function
if __name__ == '__main__':
    main()
