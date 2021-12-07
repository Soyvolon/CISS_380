# The attached file contain the skeletal code for Binary Tree class. You are 
# to add a couple of additional components to this file. First, write method 
# isBST. this method should check if a binary tree is a binary search tree returning 
# True or False accordingly. You should assume (that is you don't need to write code 
# to check it) that all data in the binary tree are of the same type and that type is comparable.

# In order to test your method you need to write a function (notice it is a 
# function not a method) makeCompleteBinaryTree. This function should take as a 
# parameter a list of data items and create and return the complete binary tree 
# with the nodes containing elements from the list. The first element of the list 
# should be the data in root node, the next two elements should be the data in 
# the level one nodes and so on. You may check your textbook for the definition 
# of the complete binary tree. 

from btnode import BTNode

def makeCompleteBinaryTree(data) -> BTNode:
    """Returns a complete binary tree for provided values.

    Args:
        data (list[any]): A list of any data types

    Returns:
        BTNode: The binary tree the return. Will be None if an invalid set of parameters
        is passed.
    """
    if not isinstance(data, list):
        return None
    if len(data) <= 0:
        return None

    node = BTNode(data[0])
    head = node

    level = [node]
    levelKey = 0
    nextLevel = []
    left = True

    if len(data) < 2:
        return head
    else:
        for i in data[1::]:
            if levelKey >= len(level):
                level = nextLevel
                nextLevel = []
                levelKey = 0

            if left:
                level[levelKey].left = BTNode(i)
                nextLevel.append(level[levelKey].left)
                left = False
            else:
                level[levelKey].right = BTNode(i)
                nextLevel.append(level[levelKey].right)
                left = True
                levelKey += 1

    return head

def main():
    left = BTNode(2, BTNode(1), BTNode(3))
    right = BTNode(8, BTNode(6, BTNode(5), BTNode(7)), BTNode(10))
    tree = BTNode(4, left, right)

    print(tree.isBST())

    left.left.data = 12

    print()
    print(tree.isBST())

    head = makeCompleteBinaryTree([1, 2, 3, 4, 5, 6, 7, 8])

    print(head)

    head = makeCompleteBinaryTree([2, 1, 3])

    print(head.isBST())


if __name__ == "__main__":
    main()
