def Merge(arr , low ,high , n , mid ):
	b =  [0 for i in range(n)] 
	k = low
	i = low 
	j = mid +1  
	while(i<=mid and j<=high):
			if(arr[i]<arr[j]):
				b[k] = arr[i]  
				k+=1 
				i+=1
			else:
				b[k] = arr[j] 
				k+=1
				j+=1  
	while(i<=mid):
		b[k] = arr[i]
		i+=1
		k+=1
	while(j<=high):
		b[k] = arr[j]
		j+=1
		k+=1 
	for i in range(low , high+1):
		arr[i] =  b[i]  
			
def MergeSort(arr , low , high  , n ):
	if(low<high):
		mid  = (low+high)//2
		MergeSort(arr ,low , mid-1 , n )
		MergeSort(arr, mid+1 ,high ,n)
		Merge(arr,low,high , n , mid)
class QueueArray:
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
			self.data[self.rear] = data 
			self.count +=1
			return 
		elif(self.rear== self.size-1):
			print("Queue is full ") 
		else :
			self.rear +=1
			self.data[self.rear] =  data
			self.count+=1
		MergeSort(self.data , 0 , self.count-1,self.count)
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