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


def Solution(s, n, k):
    # Write Your Code Here
    countW = 0
    tmpStore = []
    for c in s:
        if c == "W":
            countW += 1
    if countW == 0:
        print(max(0, (2*k)-1))
    else:
        countW += k
        if countW >= n:
            print(max(0, (2*n)-1))

        else:
            l = 0
            for c in s:
                if c == "L":
                    l += 1
                else:
                    tmpStore.append(l)
                    l = 0
            if l != 0:
                tmpStore.append(l)

            if len(tmpStore) and s[0] == "L":
                tmpStore.pop(0)
            if len(tmpStore) and s[-1] == "L":
                tmpStore.pop()
            sp = 0
            i = 0
            tmpStore = sorted(tmpStore)
            while i < len(tmpStore):
                if tmpStore[i]+sp > k:
                    break
                sp += tmpStore[i]
                i += 1
            wl = len(tmpStore)-i
            ans = (2*countW) - wl-1
            print((max(ans, 0)))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        Solution(s, n, k)


# calling main Function
if __name__ == '__main__':
    main()
