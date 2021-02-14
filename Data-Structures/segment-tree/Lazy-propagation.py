class LazyProgagation():
    def __init__(self, size):
        self.tree = [0 for _ in range(4*size)]
        self.propagation = [0 for _ in range(4*size)]

    def create(self, arr):
        self.createHelper(arr, self.tree, 0, len(arr)-1, 0)

    def createHelper(self, arr, tree, start, end, treeNode):
        # createHelper(self,arr,)
        if start == end:
            tree[treeNode] = arr[start]
            return
        mid = (start+end)//2
        self.createHelper(arr, tree, start, mid, 2*treeNode+1)
        self.createHelper(arr, tree, mid+1, end, 2*treeNode+2)
        tree[treeNode] = tree[2*treeNode+1]+tree[2*treeNode+2]

    def update(self, frm, to, val, n):
        self.updateHelper(0, n-1, frm, to, 0, val)

    def updateHelper(self, start, end, frm, to, treeNode, value):
        # updateHelper(self,arr,)
        if self.propagation[treeNode] != 0:
            v = self.propagation[treeNode]
            self.tree[treeNode] += v
            self.propagation[treeNode] = 0
            if start != end:
                self.propagation[2*treeNode+1] += v
                self.propagation[2*treeNode+2] += v
        if start > end or start < to or end < frm:
            return
        if start >= frm and end <= to:

            self.tree[treeNode] += value
            if start != end:
                self.propagation[2*treeNode+1] += value
                self.propagation[2*treeNode+2] += value
            return
        mid = (start+end)//2
        self.updateHelper(start, mid, frm, to, 2*treeNode+1, value)
        self.updateHelper(mid+1, end, frm, to, 2*treeNode+2, value)
        self.tree[treeNode] = self.tree[2*treeNode+1]+self.tree[2*treeNode+2]

    def getRange(self, start, end, treeNode, left, right):
        if start > right or end < left:
            return 0
        if start >= left and end <= right:
            return self.tree[treeNode]
        mid = (start+end)//2
        return self.getRange(start, mid, 2*treeNode+1, left, right)+self.getRange(mid+1, end, 2*treeNode+2, left, right)

    def printTree(self):
        for v in self.tree:
            if v:
                print(v, end=" ")
        print("")


# // Initialize
n, q = map(int, input().split())
arr = list(map(int, input().split()))
sg = LazyProgagation(n)
sg.create(arr)
for _ in range(q):
    l, r = map(int, input().split())
    print(sg.getRange(0, n-1, 0, l, r))
