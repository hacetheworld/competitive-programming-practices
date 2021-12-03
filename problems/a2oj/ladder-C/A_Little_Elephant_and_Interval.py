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

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def getSum(n):
    if n <= 9:
        return n
    ln = len(str(n))
    ans = 9
    for i in range(ln-1, 1, -1):
        ans += (9*10**(i-2))
    ans += ((int(str(n)[0])-1)*10**(ln-2))
    digits = []
    t = n
    while t > 0:
        digits.append(t % 10)
        t = t//10
    digits.pop(0)
    digits.pop()
    digits = list(reversed(digits))
    # tmpAns = 1
    if ln >= 3:
        for i in range(len(digits)):
            v = digits[i]
            # print(v*(10**(ln-(3+i))), "endm")
            ans += (v*(10**(ln-(3+i))))

    if int(str(n)[0]) > int(str(n)[-1]):
        return ans
    else:
        return ans+1


def Solution():
    # Write Your Code Here
    l, r = get_ints_in_variables()
    if r <= 9:

        print(r-(l-1))
        return
    print(getSum(r)-getSum(l-1))


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
