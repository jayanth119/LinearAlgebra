class Node:
    def __init__(self, data):
        self.data = data
        self.Nxt = None


class StackLL:
    """docstring for """

    def __init__(self):
        self.root =	None
        self.top = None
        self.count = -1

    def push(self, data):
        if (self.root == None):
            new = Node(data)
            self.root = new
            self.top = new 
            self.count += 1
            return 
        
        x = Node(data) 
        x.Nxt = self.top 
        self.top = x
        self.count+=1
    def pop(self):
        n = None
        if self.count== -1:
            return -1
        else:
            self.count -= 1
            n = self.top
            self.top = self.top.Nxt
            return n.data 

    def peek(self):
        if self.root == None:
            return -1
        return self.root.data

    def display(self):
        if (self.top == -1):
            print("stack is empty")
        else:
            p = self.top
            while (p != None):
                print(p.data)
                p = p.Nxt
