def Solution(arr, K):
    # Solution
    for i in range(len(arr)):
        if arr[i] == K:
            return i+1
    return -1


# for t in range(int(input())):
N = int(input())
arr = list(map(int, input().split()))
K = int(input())
# strArr = [input() for _ in range(N)]
# print("Case #{}: {}".format(t+1, Solution(arr)))
print(Solution(arr, K))
