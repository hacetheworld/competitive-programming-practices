def maxtrixMultipication(A, B):
    n = len(A)
    m = len(A[0])
    op = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp = 0
            for k in range(m):
                temp += (A[i][k]*B[k][j])
            op[i][j] = temp
    for i in range(n):
        for j in range(m):
            A[i][j] = op[i][j]
    # print(A)


def power(A, n):
    if n == 0 or n == 1:
        return
    power(A, n//2)
    maxtrixMultipication(A, A)
    if n % 2 != 0:
        mn = [[1, 1], [1, 0]]
        maxtrixMultipication(A, mn)


def matrixExponantion(n):
    A = [[1, 1], [1, 0]]
    power(A, n-1)
    print(A[0][0])


n = int(input())
matrixExponantion(n)
