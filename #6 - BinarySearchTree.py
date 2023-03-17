"""BinarySearchTree"""

class BSTNode:
    """Binary Search Tree Node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree"""
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

    def delete(self, data):
        """Delete Node in Binary Search Tree"""
        start = self.root
        prev = None
        if self.is_empty():
            print("This tree is empty!!")
        else:
            while start.data != data:
                if data < start.data:
                    prev = start
                    start = start.left
                elif data > start.data:
                    prev = start
                    start = start.right
            if start.left is None and start.right is None:
                if start.data != self.root.data:
                    if start.data < prev.data:
                        prev.left = None
                    elif start.data > prev.data:
                        prev.right = None
                else:
                    self.root = None
            elif start.left is None and start.right is not None:
                if start.data != self.root.data:
                    prev.left = start.right
                    start.right = None
                else:
                    self.root = start.right
            elif start.right is None and start.left is not None:
                if start.data != self.root.data:
                    prev.right = start.left
                    start.left = None
                else:
                    self.root = start.left
            else:
                if start.data != self.root.data:
                    start2 = start.left
                    prev2 = None
                    while start2.right is not None:
                        prev2 = start2
                        start2 = start2.right
                    start.data = start2.data
                    prev2 = None
                else:
                    start3 = start.left
                    prev3 = None
                    while start3.right is not None:
                        prev3 = start3
                        start3 = start3.right
                    if prev3 is not None:
                        self.root.data = start3.data
                        prev3.right = None
                    else:
                        self.root.data = start3.data
                        self.root.left = None
        return data


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
        if self.is_empty():
            print("This tree is empty!!")
        else:
            start = self.root
            while start.left != None:
                start = start.left
            return start.data

    def findMax(self):
        """Find Maximum of Binary Search Tree"""
        if self.is_empty():
            print("This tree is empty!!")
        else:
            start = self.root
            while start.right != None:
                start = start.right
            return start.data

myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.insert(5)
myBST.insert(20)
myBST.insert(13)
# print(myBST.findMin())
# print(myBST.findMax())
print(myBST.delete(5))
print(myBST.delete(33))
print(myBST.delete(14))
print(myBST.delete(7))
print(myBST.delete(23))
print(myBST.delete(13))
print(myBST.delete(10))
# print(myBST.delete(20))
myBST.traverse()