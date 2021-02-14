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
    parent = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]
    while True:
        inp = input()
        if inp == "exit":
            return
        if inp == "union":
            a, b = get_ints_in_variables()
            union(parent, rank, a, b)
        else:
            a = int(input())
            print(get(parent, a))


#  call the main method  pa
if __name__ == "__main__":
    main()
