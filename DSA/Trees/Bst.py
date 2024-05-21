class  Node():
	def __init__(self, data ):
		self.data = data 
		self.Lchild = None 
		self.Rchild = None 
class Bst(object):
	def __init__(self):
		self.root = None 
	def insert(self , data ):
		if(self.root == None ) : 
			self.root = Node(data)
			return 
		current = self.root 
		p = None 
		new = Node(data) 
		while(current!=None ): 
			p = current 
			if(data < current.data ):
				current = current.Lchild
			elif (data > current.data):
				current = current.Rchild 
		if(p == None ):
			p = new 
		elif(p.data <  data ):
			p.Lchild = new 
		elif (p.data > data ): 
			p.Rchild = new 


root = Bst() 
root.insert(69)
root.insert(79)
print("hello world ")