class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class DoubleCircularLinkedList:
    root  = None
    def __init__(self):
        self.root = None
        self.count = 0
    def insertlast(self,data):
        if(self.root ==None):
            self.root = Node(data)
            self.root.right  = self.root
        else :
            p = self.root.right
            while(p.right!=self.root):
                p = p.right
            new = Node(data)
            new.left = p
            p.right = new 
            new.right = self.root
        self.count+=1
    def insertfirst(self,data):
        if(self.root==None):
            self.root = Node(data)
            self.root.right = self.root
        else :
            p = self.root.right
            new = Node(data)
            self.root.left = new
            new.right = self.root
            while(p.right!=self.root):
                p = p.right
            p.right = new
            self.root = new
        self.count+=1
    def insertbtw(self , data ,i=0):
        temp = self.root
        if(i>self.count or i< 0 ):
            print("it is impossible to insert ")
            return
        elif(i==self.count):
            self.insertlast(data)
        elif(self.root is None ):
            self.root = Node(data)
            self.root.Node = self.root 
        elif(i== 0 ):
            self.insertfirst(data)
        else :
            x = 0
            while(x!=i-2 and temp !=None):
                temp = temp.RNode
                x+=1
            p = temp.right
            new = Node(data)
            new.right = p 
            p.left =  new
            new.left = temp 
            temp.right = new 
        self.count +=1
    def insert(self,data ,place = -1):
        if(place == -1 ):
            self.insertlast(data)
        elif(place == 1):
            self.insertfirst(data)
        elif(place > 1 and place<self.count):
            self.insertbtw(data,place)
        else :
            print("invalid\n")
    def deletelast(self):
        if(self.root == None):
            print("empty")
            return
        elif(self.root.right==self.root):
            self.root = None             
        else:
            p  =self.root.right
            q = self.root 
            while(p.right!=self.root):
                q = q.right
                p = p.right
            q.right = self.root
        self.count-=1
    def deletefirst(self):
        if(self.root==None):
            print("empty")
            return
        elif(self.root.right==self.root):
            self.root = None
        else :
            p  = self.root.right
            q = p
            while(p.right!=self.root):
                p = p.right
            p.right = q
            q.left = None
            self.root  =  q
        self.count-=1
    def deletebtw(self,i = -1 ):
        if(i==-1):
            self.deletelast()
        elif(i==1):
            self.deletefirst()
        elif(i>self.count):
            print("it is impossible to delete ")
            return
        else :
            c  = 0
            p = self.root
            while(c!=i-2):
                p = p.right
                c+=1
            q = p.right
            c = q.data 
            q.right.left = p
            p.right = q.right
            self.count-=1 
            return c
    def delete(self , i = -1 ):
        if(i==-1):
            self.deletelast()
        elif( i == 1):
            self.deletefirst()
        elif( i > 1 and  i <self.count):
            self.deletebtw( i )
        else :
            print("invalid\n")           
    def display(self):
        if(self.root == None ):
            print("empty")
        else :
            p =self.root.right
            print(self.root.data,end='->')
            while(p!=self.root):
                print(p.data,end="->")
                if(p.right==self.root):
                    print(self.root.data)
                p = p.right
    def TotalNodes(self):
        return self.count
    
root = DoubleCircularLinkedList()
root.insertlast(1)
root.insertlast(2)
root.insertlast(3)
root.insertlast(4)
root.insertlast(5)
root.insertlast(6)
root.deletebtw(4)
root.display()
print("hello")
print("the total no of nodes ",root.TotalNodes())
