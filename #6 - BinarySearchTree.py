"""BinarySearchTree"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        """Check if Binary Search Tree is Empty or not"""
        if self.root == None:
            return True
        else:
            return False

    def insert(self, data):
        """Insert BSTNode in BST"""
        pNew = BSTNode(data)
        start = self.root
        prev = None
        if self.is_empty():
            self.root = pNew
        else:
            while start != None:
                if data < start.data:
                    prev = start
                    start = start.left
                elif data > start.data:
                    prev = start
                    start = start.right
            if data < prev.data:
                prev.left = pNew
            elif data > prev.data:
                prev.right = pNew
        return

    def preorder(self, root):
        """Preorder"""
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        """Inorder"""
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        """Postorder"""
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self):
        """Traverse in Binary Search Tree"""
        if self.is_empty():
            print("This tree is empty!!")
        else:
            print("Preorder : ")
            self.preorder(self.root)
            print("")
            print("Inorder : ")
            self.inorder(self.root)
            print("")
            print("Postorder : ")
            self.postorder(self.root)
            print("")
    
    def findMin(self):
        """Find Minimum of Binary Search Tree"""
        start = self.root
        prev = None
        while start != None:
            prev = start
            start = start.left
        return prev.data

    def findMax(self):
        """Find Maximum of Binary Search Tree"""
        start = self.root
        prev = None
        while start != None:
            prev = start
            start = start.right
        return prev.data

myBST = BST()
myBST.insert(10)
myBST.insert(20)
myBST.insert(5)
myBST.insert(25)
myBST.insert(3)
print(myBST.findMin())
print(myBST.findMax())
myBST.traverse()