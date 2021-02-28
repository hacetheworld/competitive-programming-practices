# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

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


def get_string_list_of_list(
    n): return [[c for c in input()] for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def check(matrix, r, c, n):
    if r < n-1 and c < n-1:
        if matrix[r][c+1] == "1":
            return True
        elif matrix[r+1][c] == "1":
            return True
    LeftFlag = True
    for i in range(c+1, n):
        if matrix[r][i] != "1":
            LeftFlag = False
            break
    rightFlag = True
    for i in range(r+1, n):
        if matrix[i][c] != "1":
            rightFlag = False
            break
    if LeftFlag or rightFlag:
        return True
    else:
        return False


def Solution(matrix, n):
    # visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "1":
                if not check(matrix, i, j, n):
                    print("NO")
                    return
    print("YES")


def main():
    # //Write Your Code Here
    for _ in range(get_int()):
        n = get_int()
        matrix = get_string_list_of_list(n)
        Solution(matrix, n)


#  calling main Function
if __name__ == "__main__":
    main()
