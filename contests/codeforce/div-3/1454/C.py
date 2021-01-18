def Solution(arr, n):
    hashMap = {}
    for i in range(len(arr)):
        v = arr[i]
        if v in hashMap:
            hashMap[v].append(i)
        else:
            hashMap[v] = [i]
    minRes = float("inf")
    for j in hashMap:
        item = hashMap[j]
        temp = 0
        for k in range(1, len(item)):
            prev = item[k-1]
            if item[k]-1 != prev:
                temp += 1
        if item[0] > 0:
            temp += 1
        if item[-1] < len(arr)-1:
            temp += 1
        minRes = min(minRes, temp)
    if minRes == float("inf"):
        print(0)
    else:
        print(minRes)


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # UnCOMMENT FOR TESTING IN VSCODE
    # print("<<<<<<<<<<<<<<<<-START->>>>>>>>>>>>>>>>>>>>")
    # Solution(arr, N)
    # print("<<<<<<<<<<<<<<<<-END->>>>>>>>>>>>>>>>>>>>")
    # SUBMIT FOR SOLUTION
    Solution(arr, N)
