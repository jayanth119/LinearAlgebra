class Node:
    """docstring for Node"""

    def __init__(self, arg):
        self.data = arg
        self.Lchild = None
        self.Rchild = None


class Tree:
    def createBinaryTree(self):
        self.new = Node(-1) 
        print("enter root element -1 for exit  ")
        x = int(input()) 
        if(x==-1):
            return None
        self.new.data = x 
        print("left  side ")
        self.new.Lchild = self.createBinaryTree() 
        print("right side ")
        self.new.Rchild = self.createBinaryTree() ; 
        return self.new 
c = Tree()
root = c.createBinaryTree()