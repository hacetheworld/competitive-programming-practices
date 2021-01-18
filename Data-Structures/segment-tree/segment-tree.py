class SegmentTree():
    def __init__(self, size):
        self.tree = [0 for _ in range(4*size)]

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

    def update(self, idx, v, n):
        self.updateHelper(0, n, 0, idx, v)

    def updateHelper(self, start, end, treeNode, idx, v):
        # updateHelper(self,arr,)
        if start == end:
            self.tree[treeNode] = v
            return
        mid = (start+end)//2
        if idx <= mid:
            self.updateHelper(start, mid, 2*treeNode+1, idx, v)
        else:
            self.updateHelper(mid+1, end, 2*treeNode+2, idx, v)
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
arr = [1, 2, 3, 4, 5]
n = len(arr)
sg = SegmentTree(n)
sg.create(arr)
sg.printTree()
sg.update(2, 10, n-1)
sg.printTree()
print(sg.getRange(0, n-1, 0, 1, 3))
