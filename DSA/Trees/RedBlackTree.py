# Node class for the red-black tree
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1 represents red, 0 represents black

# Red-Black Tree class
class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)  # Sentinel node
        self.root = self.nil

    def insert(self, key):
        node = Node(key)
        node.left = self.nil
        node.right = self.nil
        node.color = 1  # New nodes are always red

        # Perform a standard BST insertion
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Fix any violations in the red-black tree
        if node.parent is None:
            node.color = 0  # Root node is always black
        elif node.parent.parent is not None:
            self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == 1:
                    node.parent.color = 0
                    y.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent.left
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == 1:
                    node.parent.color = 0
                    y.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent.right
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)

        self.root.color = 0  # Root is always black

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def delete(self, key):
        node = self.find(key)
        if node == self.nil:
            return

        if node.left != self.nil and node.right != self.nil:
            successor = self.minimum(node.right)
            node.key = successor.key
            node = successor

        # At this point, node has at most one child

        child = node.left if node.left != self.nil else node.right
        self.transplant(node, child)

        if node.color == 0:
            self.delete_fixup(child)

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete_fixup(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                sibling = node.parent.right

                if sibling.color == 1:
                    sibling.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    node = node.parent
                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.right_rotate(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = 0
                    sibling.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left

                if sibling.color == 1:
                    sibling.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == 0 and sibling.left.color == 0:
                    sibling.color = 1
                    node = node.parent
                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.left_rotate(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 0
                    sibling.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root

        node.color = 0
    def find(self, key):
        current = self.root
        while current != self.nil:
            if current.key == key:
                return current
            elif current.key > key:
                current = current.left
            else:
                current = current.right

        return self.nil

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node


    def in_order_traversal(self):
        def traverse(node):
            if node != self.nil:
                traverse(node.left)
                print(node.key, end=' ')
                traverse(node.right)

        traverse(self.root)



root  = RedBlackTree()
root.insert(69)
root.insert(30)
root.insert(70)
root.delete(70)
root.in_order_traversal()












    
