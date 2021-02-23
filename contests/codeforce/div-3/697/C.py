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


def Solution(boys, girls, a, b, k):
    cntBoys = [0 for _ in range(a+1)]
    cntGirls = [0 for _ in range(b+1)]
    for v in boys:
        cntBoys[v] += 1
    for u in girls:
        cntGirls[u] += 1
    cnt = 0
    for i in range(k):
        cnt += k-(cntBoys[boys[i]]+cntGirls[girls[i]])+1
    print(cnt//2)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        a, b, k = get_ints_in_variables()
        boys = get_ints_in_list()
        girls = get_ints_in_list()
        Solution(boys, girls, a, b, k)


# call the main method
if __name__ == "__main__":
    main()
