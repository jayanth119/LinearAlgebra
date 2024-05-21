class Node:
    def __init__(self,data ):
        self.data = data
        self.LNode = None
        self.RNode = None
class DoubleLinkedList:
    root = None 
    def __init__(self):
        self.root = None
        self.count = 0
    def insertlast(self, data ):
        if(self.root is None ):
            self.root = Node(data)
            self.count +=1 
        else:
           temp = self.root
           while(temp.RNode!=None):
               temp = temp.RNode
           new = Node(data)
           new.LNode = temp
           temp.RNode = new
           self.count +=1 

    def insertfirst(self,data):
        if(self.root is None ):
            self.root = Node(data) 
            self.count+=1 
        else :
            new = Node(data)
            self.root.LNode = new
            new.RNode = self.root
            self.root = new
            self.count +=1 

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
            self.count+=1
        elif(i== 0 ):
            self.insertfirst(data)
            self.count+=1 
        else :
            x = 0
            while(x!=i-2 and temp !=None):
                temp = temp.RNode
                x+=1
            p = temp.RNode
            new = Node(data)
            new.RNode = p 
            p.LNode =  new
            new.LNode = temp 
            temp.RNode = new 
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
    def deletefirst(self):
        c = -1 
        if(self.root.RNode is None):
            self.root = None 
            self.count-=1 
        elif(self.root  is   None)== False :
            c = self.root.data
            self.root = self.root.RNode
            self.root.LNode = None 
            self.count-=1 
        return c 
    def deletelast(self):
        c = -1
        if(self.root==None):
            return -1
        elif(self.root.RNode is None ):
            c = self.root.data
            self.count-=1
            self.root = None
            return c
        else :
            p = self.root
            q = self.root.RNode 
            while(q.RNode!= None):
                p = p.RNode
                q = q.RNode
            self.count -=1
            c = q.data 
            p.RNode = None  
            return c
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
                p = p.RNode
                c+=1
            q = p.RNode
            c = q.data 
            q.RNode.LNode = p
            p.RNode = q.RNode
            self.count-=1 
            return c

    def delete(self , i = -1 ):
        if(i==-1):
            self.deletelast()
        elif( i == 1):
            self.deletefirst()
        elif( i > 1 and  i <self.count):
            self.deletebtw(i)
        else :
            print("invalid\n")  
    def display(self):
        if(self.root is None ):
            print("empty sorry ")
            return 
        p = self.root
        while(p!=None):
            print(p.data , end=" ->")
            if(p.RNode==None):
                print("null")
            p = p.RNode
    def TotalNode(self):
        return self.count
