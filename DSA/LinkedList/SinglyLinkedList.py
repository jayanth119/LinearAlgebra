class Node:
    def __init__(self , data = None ):
        self.data = data 
        self.Node = None
class LinkedList:
    root = None 
    def __init__(self):
        self.root = None
        self.count = 0 
    def insertlast(self, data ):
        if(self.root is None ):
            self.root = Node(data)
            self.count +=1 
        else:
            current_Node = self.root
            while(current_Node.Node!=None):
                current_Node = current_Node.Node
            new = Node(data)
            current_Node.Node  = new
            self.count +=1 
    def insertfirst(self,data):
        if(self.root is None ):
            self.root = Node(data)
            self.count+=1 
        else :
            p = self.root
            new = Node(data)
            new.Node = p
            self.root = new
            self.count+=1 
    def insertbtw(self , data ,i=0):
        temp = self.root
        if(i>self.count):
            print("it is impossible to insert ")
            return
        elif(i==self.count):
            self.insertlast(data)
        elif(self.root is None  ):
            self.root = Node(data)
            self.count+=1
        elif(i==0 ):
            self.insertfirst(data) 
        else :
            x = 0
            while(x!=i-2 and temp !=None):
                temp = temp.Node
                x+=1
            p = temp.Node
            new = Node(data)
            new.Node = p
            temp.Node = new
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
        if(self.root.Node is  None  ):
            c = self.root.data 
            self.root = None 
            self.count-=1 

        elif (self.root  is   None)== False :
            c = self.root.data
            self.root = self.root.Node
            self.count-=1 
        return c
    def deletelast(self):
        c = -1
        if(self.root==None):
            return -1
        elif(self.root.Node == None):
            c = self.root.data
            self.count-=1 
            self.root = None
            return c
        else :
            p = self.root
            q = self.root.Node 

            while(q.Node!=None):
                p = p.Node
                q = q.Node
            self.count -=1
            c = q.data 
            p.Node = None
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
                p = p.Node
                c+=1
            q = p.Node
            c = q.data 
            p.Node = q.Node
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
        Temp= self.root
        if(Temp == None ):
            print("linked list is empty ")
        while(Temp!=None):
            print(Temp.data, end=" -> ")
            if(Temp.Node==None)==True:
                print("null")
            Temp = Temp.Node           
    def TotalNode(self):
        return self.count
