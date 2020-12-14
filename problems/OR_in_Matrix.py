def Solution(matrix, newMatrix, m, n):
    # Solution
    # Do it again
    pass


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
newMatrix = [[0 for _ in range(N)] for _ in range(M)]
if Solution(matrix, newMatrix, M, N):
    print("YES")
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()
else:
    print("NO")
