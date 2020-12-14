class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        arr = [v for v in C]
        for i in range(len(arr)):
            arr[i] *= B

        lo = max(arr)
        hi = sum(arr)
        res = hi
        while lo <= hi:
            mid = (lo + hi)//2

            painter = self.isValid(arr, mid)

            if painter <= A:  # I required less painter than given, so I can distribute to more painter
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1

        return (res) % 10000003

    def isValid(self, arr, mid):
        painter = 1
        workload = 0
        for item in arr:  # checking for workload
            workload += item
            if workload > mid:
                workload = item
                painter += 1
        return painter
