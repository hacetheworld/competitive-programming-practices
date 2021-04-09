def Solution(arr, query):
    # Solution
    sum = 0
    for i in range(query[0], query[1]+1):
        sum += arr[i]
    return sum


N = int(input())
arr = list(map(int, input().split()))
sums = [0]
for val in arr:
    sums.append(sums[-1]+val)
for q in range(int(input())):
    query = list(map(int, input().split()))
    print(sums[query[1]+1]-sums[query[0]])
