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


def Solution(s):
    # Write Your Code Here
    s = [c for c in s]
    stk = []
    st = set(range(len(s)))
    for i in range(len(s)):
        if s[i] in "([":
            stk.append([s[i], i])
        else:
            if len(stk):
                if stk[-1][0]+s[i] in ["(]", "[)"]:
                    stk = []
                else:
                    if i in st:
                        st.remove(i)
                    if stk[-1][1] in st:
                        st.remove(stk[-1][1])
                    stk.pop()
    for i in st:
        s[i] = " "
    s = "".join(s).split()
    ans, cnt = "", 0
    for substr in s:
        k = substr.count("[")
        if k > cnt:
            ans = substr
            cnt = k
    print(cnt)
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()
