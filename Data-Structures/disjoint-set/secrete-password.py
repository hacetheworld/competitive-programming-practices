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


def get(parent, a):
    if parent[a] == a:
        return parent[a]
    res = get(parent, parent[a])
    parent[a] = res
    return parent[a]


def union(parent, rank, a, b):
    aPar = get(parent, a)
    bPar = get(parent, b)
    if rank[aPar] == rank[bPar]:
        rank[aPar] += 1
    if rank[aPar] > rank[bPar]:
        parent[bPar] = aPar
    else:
        parent[aPar] = bPar


def main():
    # //TAKE INPUT HERE
    n = int(input())
    parent = [i for i in range(27)]
    rank = [1 for _ in range(n+1)]
    total = [false for _ in range(26)]
    current = [false for _ in range(26)]
    for _ in range(n):
        password = get_string()


#  call the main method  pa
if __name__ == "__main__":
    main()
