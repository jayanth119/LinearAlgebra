class LinearStack:
   """ stack is data is special type of datastructure  is based on first in last out FILO  """

   def __init__(self, size):
      self.data = [-1 for i in range(size)]
      self.size = size
      self.top = -1
   def push(self, data):
      if (self.top == -1):
         self.top+=1
         self.data[self.top] = data
      elif (self.top == self.size-1):
         print("stack is empty ")
         return
      else:
         self.top += 1
         self.data[self.top] = data

   def pop(self):
      c = 0
      if (self.top == -1):
         print("empty")
         return -1
      else:
         c = self.data[self.top]
         self.top -= 1
      return c

   def display(self):
      if (self.top == -1):
         print("stack is empty")
      else:
         p = self.data 
         i = self.top
         while (i != -1):
            print(p[i])
            i -= 1
   def peek(self):
                if(self.top==-1):
                        return -1
                return self.data[self.top]

   def IsEmpty(self):
      if (self.top == -1):
         return True
      return False

   def IsFull(self):
      if (self.top == -1):
         return False
      if (self.top == self.size-1):
         return True
      return False

if __name__=="main":       
      a = LinearStack(4)
      print("is stack is IsFull ",a.IsFull())
      print("is stack is IsEmpty ",a.IsEmpty()) 
      a.push(1)
      a.push(2)
      a.push(3)
      a.push(4)
      a.display()
      print("is stack is IsFull ",a.IsFull())
      print("is stack is IsEmpty ",a.IsEmpty())



      
