def Solution(N):
    arr = []
    for i in range(1, N+1, 2):
        if i >= N and N & 1:
            arr.append(i)
        else:
            arr.append(i+1)
            arr.append(i)
    if N & 1:
        temp = arr[-1]
        arr[-1] = arr[len(arr)-2]
        arr[len(arr)-2] = temp
    for v in arr:
        print(v, end=" ")
    print("")


for t in range(int(input())):
    N = int(input())
    Solution(N)
