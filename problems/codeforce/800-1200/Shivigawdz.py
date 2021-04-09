def Solution(arr, A, B):
    # Solution
    prefix = [0]
    for i in range(len(arr)):
        prefix.append(prefix[i]+arr[i])
    avg = 0
    for i in range(A, B+1):
        tmp = 0
        for j in range(i):
            tmp += arr[j]
        avg = max(avg, tmp/i)
        for k in range(i, len(arr)):
            tmp += arr[k]
            tmp -= arr[k-i]
            avg = max(avg, tmp/i)
    return avg


for t in range(int(input())):
    N, B, A = map(int, input().split())
    arr = list(map(int, input().split()))
    print(Solution(arr, A, B))
