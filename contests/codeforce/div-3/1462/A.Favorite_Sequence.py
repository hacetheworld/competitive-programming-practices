def Solution(arr):
    res = []
    i = 0
    j = len(arr)-1
    while i <= j:
        if i == j:
            res.append(arr[i])
        else:
            res.append(arr[i])
            res.append(arr[j])
        i += 1
        j -= 1
    return res


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # strArr = [input() for _ in range(N)]
    for seq in Solution(arr):
        print(seq, end=" ")
