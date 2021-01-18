def Solution(arr, n):
    hashMap = {}
    for i in range(len(arr)):
        v = arr[i]
        if v in hashMap:
            hashMap[v][1] += 1
        else:
            hashMap[v] = [i+1, 1]
    minIdx = -1
    el = float("inf")
    for j in hashMap:
        item = hashMap[j]
        key = j
        if item[1] == 1 and key < el:
            el = key
            minIdx = item[0]
    if el == float("inf"):
        print(-1)
    else:
        print(minIdx)


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    Solution(arr, N)
