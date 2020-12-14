def Solution(arr, queries):
    # Solution
    for query in queries:
        for i in range(query[0], query[1]+1):
            arr[i] += (i-query[0]+1)


N = int(input())
arr = [0 for _ in range(N+1)]
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]
M = int(input())
questions = [int(input()) for _ in range(M)]
Solution(arr, queries)
for question in questions:
    print(arr[question])
