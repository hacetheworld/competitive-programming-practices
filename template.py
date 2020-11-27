def Solution(arr):
    # Solution
    pass


for t in range(int(input())):
    N = int(input())
    arr = map(int, input().split())
    # strArr = [input() for _ in range(N)]
    print("Case #{}: {}".format(t+1, Solution(arr)))
