# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def helperFunc(memoryUnit, points, i, n, m, res, hm):
    if i >= n:
        return float("inf")
    if m <= 0:
        return res
    if i in hm:
        return hm[i]
    hm[i] = min(helperFunc(memoryUnit, points, i+1, n, m-memoryUnit[i], res+points[i], hm),
                helperFunc(memoryUnit, points, i+1, n, m, res, hm))
    return hm[i]


def Solution(memoryUnit, points, n, m):
    hm = {}
    res = helperFunc(memoryUnit, points, 0, n, m, 0, hm)
    if res == float("inf"):
        print(-1)
    else:
        print(res)


def main():
    # //TAKE INPUT HERE
    t = int(stdin.readline())
    # print(t)
    for _ in range(t):
        n, m = get_ints_in_variables()
        arr1 = get_ints_in_list()
        arr2 = get_ints_in_list()
        # FIND ANSWER HERE
        Solution(arr1, arr2, n, m)
        # PRINT OUTPUT HERE


# call the main method
if __name__ == "__main__":
    main()
