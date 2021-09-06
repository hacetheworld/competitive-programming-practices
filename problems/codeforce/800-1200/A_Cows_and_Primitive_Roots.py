import sys
import math
from sys import stdin, stdout

# SOE(helper function of get gcd)


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

# get prime number form 1 to N


def getPrime(N):
    primes = sieve(N)
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)
    return result


mod = 1000000007
# gcd of two numbers


def pow(a, ex):
    if ex == 0:
        return 1
    if ex % 2 == 0:
        return pow(((a % mod)*(a % mod)) % mod, int(ex/2))
    else:
        return (a*pow(((a % mod)*(a % mod)) % mod, int(ex/2))) % mod


# TAKE INPUT
def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# gcd of two numbers


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    # Write Your Code Here
    p = int(input())
    x = 1
    count = 0
    # i = 1
    while x < p:
        flag = True
        for j in range(1, (p-2)+1):
            res = pow(x, j)-1
            if res % p == 0:
                flag = False
                x += 1
                break
        if flag:
            div = pow(x, p-1)-1
            if div % p == 0:
                count += 1
            x += 1
    print(count)


# for printing format
# print("Case #{}: {}".format(t+1, ans))
#  calling main Function
if __name__ == "__main__":
    main()
