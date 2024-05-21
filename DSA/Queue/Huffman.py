import heapq 
class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		# frequency of symbol 
		self.freq = freq 
		# symbol name (character) 
		self.symbol = symbol 
		# node left of current node 
		self.left = left 
		# node right of current node 
		self.right = right 
		# tree direction (0/1) 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 


# utility function to print huffman 
# codes for all symbols in the newly 
# created Huffman tree 
class HuffmanCoding:
	def printNodes(self , node, val="", di={}):
		newVal = val + str(node.huff)   
		if node.left:
			self.printNodes(node.left, newVal, di)
		if node.right:
			self.printNodes(node.right, newVal, di)   
		if not node.left and not node.right:
			di[node.symbol] = newVal   
		return di

	def Huffman(self , Text : str):
		chars = [] 
		for i in Text :
			if(i not in chars ):
				chars.append(i)
		freq = []
		for i in chars :
			freq.append(Text.count(i))
		nodes = [] 
		for x in range(len(chars)): 
			heapq.heappush(nodes, node(freq[x], chars[x])) 
		while len(nodes) > 1: 
			left = heapq.heappop(nodes) 
			right = heapq.heappop(nodes) 
			left.huff = 0
			right.huff = 1
			newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

			heapq.heappush(nodes, newNode)
				# Huffman Tree is ready!
		return self.printNodes(nodes[0],)
		
	def OgCost(self ,Text : str ):
		return len(Text)*8
	def HuffCost(self ,Text: dict , string : str):
		count = 0 
		for i in string: 
			count +=len(Text[i])
		return count
Y = HuffmanCoding()
t = Y.Huffman("jayanth")
print(t)
print( Y.OgCost("jayanth"))
print(Y.HuffCost(t, "jayanth"))













