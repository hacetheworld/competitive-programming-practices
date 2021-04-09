def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def Solution(arr, N):
    pass


N = int(input())
arr = list(map(int, input().split()))
print(Solution(arr, N))
