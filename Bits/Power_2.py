def Solution(arr):
    # Solution

    count = 0
    for v in arr:
        if v & 1 == 0:
            count += 1
        if v == 1:
            count += 1
    print(count)


N = int(input())
arr = [int(input()) for _ in range(N)]
Solution(arr)
