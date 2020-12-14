def sieveUpdated(N):
    primeNumbers = [True]*(N+1)
    primeNumbers[0] = False
    primeNumbers[1] = False
    ans = [0]*(N+1)
    for i in range(2, N+1):
        if primeNumbers[i]:
            count = 1
            j = i*i
            while j <= N:
                if primeNumbers[j]:
                    count += 1
                primeNumbers[j] = False
                j += i
            ans[i] = count
    return ans


# def Solution(X):
#     # Solution
#     return


ans = sieveUpdated(pow(10, 6))
# print(ans)
for t in range(int(input())):
    N = int(input())
    print(ans[N])
