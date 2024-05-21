class Node:
	def __init__(self,data):
		self.data = data 
		self.Nxt = None 
class QueueLList:
	"""docstring for QueueLList"""
	def __init__(self,size):
		self.size = size 
		self.root = None 
		self.front = None 
		self.rear = None
		self.count = 0 
	def Enqueue(self,data):
		if(self.root == None):
			self.root = Node(data)
			self.front = self.root 
			self.rear = self.root 
			self.count +=1
		elif(self.isfull()):
			print("QueueLList is full ")
		else : 
			new = Node(data) 
			self.rear.Nxt = new 
			self.rear = new
			self.count+=1 
	def  Dequeue(self):
		if(self.front==self.rear  and self.front == None ):
			print("QueueLList is empty ")
			return
		elif(self.count ==2 ):
			self.front = self.front.Nxt
		else : 
			self.front  = self.front.Nxt 
			self.count-=1 
	def isempty(self):
		return self.root==None 
	def isfull(self):
		return self.count == self.size 
	def display(self):
		p = self.front 
		q = self.rear 
		if(p== None or q == None):
			print("Queue is empty ")
			return 
		elif(p==q ):
			print(self.front.data)
		else:
			while(p!=q):
				print(p.data,end="->")
				if(p.Nxt== q ):
					print(p.Nxt.data)
					

				p=p.Nxt 
			print()
c = QueueLList(5) 
while(True):
	print("1 enqueue")
	print("2 dequeue ")
	if(int(input("enter numbeer"))==1):
		c.Enqueue(int(input("enter data")))
		c.display()
	else :
		c.Dequeue() 
		c.display()
	