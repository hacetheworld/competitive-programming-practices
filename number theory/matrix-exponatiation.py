def matrixMultiply(matrix):
    newMatrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            csum = 0
            for k in range(len(matrix)):
                csum += (matrix[i][k]*matrix[k][j])
            newMatrix[i][j] = csum
    return newMatrix


def calculateValue(matrix, r, c):
    val = 0
    length = len(matrix)
    while c < length:
        val += (matrix[c][r]*matrix[r][c])
        c += 1
    return val


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
print(matrix)
print(matrixMultiply(matrix))
