# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout
sys.setrecursionlimit(1 << 30)
# //Most Frequently Used Number Theory Concepts


def sieve(N):
    primeNumbers = [True]*(N+1)
    primeNumbers[0] = False
    primeNumbers[1] = False
    i = 2
    while i*i <= N:
        j = i
        if primeNumbers[j]:
            while j*i <= N:
                primeNumbers[j*i] = False
                j += 1
        i += 1
    return primeNumbers


def getPrime(N):
    primes = sieve(N)
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)
    return result


def factor(N):
    factors = []
    i = 1
    while i*i <= N:
        if N % i == 0:
            factors.append(i)
            if i != N//i:
                factors.append(N//i)
        i += 1
    return sorted(factors)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def extendedGcd(a, b):
    if a < b:
        return extendedGcd(b, a)
    if b == 0:
        return [a, 1, 0]
    res = extendedGcd(b, a % b)
    x = res[2]
    y = res[1]-(math.floor(a/b)*res[2])
    res[1] = x
    res[2] = y
    return res


def iterativeModularFunc(a, b, c):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % c
        a = (a*a) % c
        b = b//2
    return res

# // Taking Input Format Helper Function


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_matrix(n): return [[c for c in input()] for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def dfs(matrix, i, j, visited, s):
    if (i < 0 or i >= len(matrix)) or (j >= len(matrix[0]) or j < 0):
        return
    if visited[i][j] == False and matrix[i][j] == "B":
        print("YES")
        print(len(s))
        print(s)
        return
    if matrix[i][j] == "#" or visited[i][j] == True:
        return
    visited[i][j] = True
    dfs(matrix, i-1, j, visited, s+"U")
    dfs(matrix, i+1, j, visited, s+"D")
    dfs(matrix, i, j-1, visited, s+"L")
    dfs(matrix, i, j+1, visited, s+"R")


def Solution(matrix, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "A":
                if dfs(matrix, i, j, visited, ""):
                    return
    print("NO")


def main():
    # //Write Your Code Here
    n, m = get_ints_in_variables()
    matrix = get_matrix(n)
    Solution(matrix, n, m)


#  calling main Function
if __name__ == "__main__":
    main()
