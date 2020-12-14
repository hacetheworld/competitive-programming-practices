def Solution(matrix, query):
    # Solution
    return calculateSum(matrix, query)


def calculateSum(matrix, opration):
    startRow = opration[0]
    endRow = opration[2]
    startCol = opration[1]
    endCol = opration[3]
    sum = 0
    for row in range(startRow, endRow+1):
        for col in range(startCol, endCol+1):
            sum += matrix[row][col]
    return sum


def modefieMatrix(matrix, opration):
    val = opration[0]
    startRow = opration[1]
    endRow = opration[3]
    startCol = opration[2]
    endCol = opration[4]
    for row in range(startRow, endRow+1):
        for col in range(startCol, endCol+1):
            matrix[row][col] += val


M, N, U, Q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
modifications = [list(map(int, input().split())) for _ in range(U)]
queries = [list(map(int, input().split())) for _ in range(Q)]
for opration in modifications:
    modefieMatrix(matrix, opration)
prefixSum = [[0 for _ in range(N)] for _ in range(M)]
prefixSum[0][0] = matrix[0][0]
for i in range(len(prefixSum)):
    for j in range(len(prefixSum)):
        if i == 0 and j == 0:
            continue
        if i == 0 and j != 0:
            prefixSum[i][j] = prefixSum[i][j-1]+matrix[i][j]
            prefixSum[j][i] = prefixSum[j-1][i]+matrix[j][i]

        elif i != 0 and j != 0:
            prefixSum[i][j] = (prefixSum[i][j-1] + prefixSum[i-1]
                               [j]-prefixSum[i-1][j-1]) + matrix[i][j]
for query in queries:
    r1 = query[0]
    r2 = query[2]
    c1 = query[1]
    c2 = query[3]
    ans = prefixSum[r2][c2]
    if r1-1 >= 0:
        ans -= prefixSum[r1-1][c2]
    if c1-1 >= 0:
        ans -= prefixSum[r2][c1-1]
    if r1-1 >= 0 and c1-1 >= 0:
        ans += prefixSum[r1-1][c1-1]

    print(ans)
