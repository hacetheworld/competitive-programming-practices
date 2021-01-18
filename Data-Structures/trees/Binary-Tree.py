class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.size = 0
        self.root = self.createBinaryTree(None, True)

    def createBinaryTree(self, parent, ilc):
        if parent == None:
            print("Give Parent Value ")
        else:
            if ilc:
                print("Enter Left Child Value of ", parent.data)
            else:
                print("Enter Right Child Value ", parent.data)
        v = int(input())
        newNode = Node(v)
        self.size += 1
        print(newNode.data, " Has Left Child ?")
        hlc = input()
        if hlc == "True":
            newNode.left = self.createBinaryTree(newNode, True)

        print(newNode.data, " Has Right Child ?")
        hrc = input()
        if hrc == "True":
            newNode.right = self.createBinaryTree(newNode, False)
        return newNode

    def preorderTraversal(self, root, res):
        if root:
            res.append(root.data)
            self.preorderTraversal(root.left, res)
            self.preorderTraversal(root.right, res)

    def inorderTraversal(self, root, res):
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.data)
            self.inorderTraversal(root.right, res)

    def postorderTraversal(self, root, res):
        if root:
            self.postorderTraversal(root.left, res)
            self.postorderTraversal(root.right, res)
            res.append(root.data)

    def display(self):
        print("-------------")
        self.displayHelper(self.root)
        print("-------------")

    def displayHelper(self, root):
        if root == None:
            return
        st = ""
        if root.left == None:
            st += "."
        else:
            st += str(root.left.data)
        st += "=> "+str(root.data)+" <="
        if root.right == None:
            st += "."
        else:
            st += str(root.right.data)
        print(st)
        self.displayHelper(root.left)
        self.displayHelper(root.right)

    def levelOrder(self):
        queue = []
        res = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(res)


BinaryTreeObj = BinaryTree()
BinaryTreeObj.levelOrder()
