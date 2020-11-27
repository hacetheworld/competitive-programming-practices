def Solution(arr):
    # Solution
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]:
                pass


for t in range(int(input())):
    N = int(input())
    arr = map(int, input().split())
    print(Solution(arr))
