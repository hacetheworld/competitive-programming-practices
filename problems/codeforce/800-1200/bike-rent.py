def Solution(boys_money, bike_rent, schoolBoys, bikes, sharedBudget):
    # Solution
    l = 0
    r = bikes
    prefixSum = [0]
    for bm in boys_money:
        prefixSum.append(prefixSum[-1]+bm)
    totalSum = sharedBudget+sum(boys_money)
    ans = [0, 0]
    while l <= r:
        mid = (l+r)//2
        res = canBuy(bike_rent, mid, totalSum-prefixSum[mid])
        if res[0]:
            l = mid+1
            ans = (mid, abs(sharedBudget-res[1]))
        else:
            r = mid-1
    return ans


def canBuy(bike_rent, mid, totalSum):
    tempSum = 0
    for i in range(mid):
        tempSum += bike_rent[i]
        if tempSum > totalSum:
            return [False, 0]
    return [True, tempSum]


N, M, A = map(int, input().split())
boys_money = sorted(list(map(int, input().split())), reverse=True)
bike_rent = sorted(list(map(int, input().split())))
res = Solution(boys_money, bike_rent, N, M, A)
print(res[0], res[1])
