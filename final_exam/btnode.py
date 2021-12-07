# The attached file contain the skeletal code for Binary Tree class. You are 
# to add a couple of additional components to this file. First, write method 
# isBST. this method should check if a binary tree is a binary search tree returning 
# True or False accordingly. You should assume (that is you don't need to write code 
# to check it) that all data in the binary tree are of the same type and that type is comparable.

class BTNode(object):
    """Represents a node for a linked binary tree."""

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self, 0)
    def set_left(self, leftChild):
        self.left = leftChild
    def set_right(self, rightChild):
        self.right = rightChild
    def set_data(self, newData):
        self.data = newData

    def isBST(self) -> bool:
        if isinstance(self.left, BTNode):
            if self.left.data >= self.data:
                return False
            else:
                return self.left.isBST()
        if isinstance(self.right, BTNode):
            if self.right.data <= self.data:
                return False
            else:
                return self.right.isBST()
        return True