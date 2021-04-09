def power(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        b = b//2
    return res


def factorial(fact, n, mod):
    for i in range(1, n+1):
        fact[i] = ((i % mod) * (fact[i-1]) % mod) % mod


def ncr(fact, n, r, mod):
    if r > n | n < 0 | r < 0:
        return 0
    return (fact[n] % mod)*(power(fact[r], mod-2, mod) % mod)*(power(fact[n-r], mod-2, mod) % mod) % mod


def main():
    n = 10
    prime = pow(10, 9)+7
    fact = [1 for _ in range(n+1)]
    factorial(fact, n, prime)
    print(ncr(fact, 4, 2, prime))


if __name__ == "__main__":
    main()
