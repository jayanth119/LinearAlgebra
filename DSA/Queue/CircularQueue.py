class CQueueArray:
	"""docstring for QueueArray"""
	def __init__(self, arg):
		self.data = [ 0 for i in range(arg)]
		self.count = 0 
		self.size = arg  
		self.front = -1 
		self.rear  = -1
	def Enqueue(self, data ):
		if(self.rear==-1):
			self.rear +=1
			self.front +=1
			self.data[self.rear%self.size] = data 
			self.count +=1
			return 
		elif(self.rear== self.size):
			print("Queue is full ") 
		else :
			self.rear +=1
			self.data[self.rear] =  data
			self.count+=1
	def isFull(self):
		return self.count==self.size 
	def isempty(self):
		return self.front == -1 
	def Dequeue(self):
		c = 0 
		if(self.front==-1 or self.front>self.rear ):
			print("Queue is empty ")
			return
		elif(self.front+1 == self.size):
			c = self.data[self.front] 
			self.count-=1
			self.front = -1
			self.rear =  -1 
			return c 
		self.count-=1
		c = self.data[self.front]
		self.front +=1  
		return c 
	def display(self):
		p = self.front 
		q = self.rear 
		if(p==-1  ) or ((p+1==self.size and p!=-1)):
			print("Queue is empty ")
			return 
		elif(self.front<=self.rear):
			while(p<=q):
				print(self.data[p],end="--")
				# if(p+1 == q ):
				# 	print(self.data[p+1])
					

				p+=1 
			print()
