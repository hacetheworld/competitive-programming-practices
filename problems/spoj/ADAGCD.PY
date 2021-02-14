# import inbuilt standard input output
import sys
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


# Sieve of erthonisis(I know it's wrong spelleing)
def sieve(N):
    primeNumbers = [0]*(N+1)
    primeNumbers[2] = 1
    for i in range(2, N):
        if primeNumbers[i]:
            for j in range(2*i, N):
                primeNumbers[j] = i
    return primeNumbers


maxl = int(10e7+1)


def main():
    # //TAKE INPUT HERE
    n = int(stdin.readline())
    primes = sieve(maxl)
    print(primes)
    elemation = []
    # print(t)
    for k in range(n):
        mi = get_ints_in_variables()
        mp = [0 for _ in range(maxl)]
        for _ in range(0, mi):
            d = int(input())
            while d > 1:
                mp[primes[d]] += 1
                d = d//primes[d]
        if k == 0:
            elemation.copy(mp)
        else:
            for i in range(len(mp)):
                if mp[i] != 0:
                    elemation[i] = min(mp[i], elemation[i])

    print(elemation)


# call the main method
if __name__ == "__main__":
    main()
