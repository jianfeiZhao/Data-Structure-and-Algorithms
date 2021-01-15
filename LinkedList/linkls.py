class Node(object):

	def __init__ (self, x):
		self.data = x
		self.next = None

	def get_next (self):
		return self.next

	def set_next (self, n):
		self.next = n
		
	def get_data (self):
		return self.data

	def set_data (self, x):
		self.data = x
		
	def has_next (self):
		if self.get_next() is None:
			return False
		return True
		
	def to_string (self):
		return "Node value: " + str(self.data)
		
class LinkedList (object):

	def __init__ (self, r = None):
		self.root = r
		self.size = 0

	def get_size (self):
		return self.size

	def add (self, d):       
		# add node with data d points to pre root
		self.add_node(Node(d))
		#new_node.set_next = self.root
		#self.root = new_node
		#self.size += 1

	def add_node (self, n):   
		# add node points to pre root
		n.set_next(self.root)
		self.root = n
		self.size += 1
		
	def remove (self, d):
		# remove a node with data d
		this_node = self.root
		prev_node = None

		while this_node is not None:
			if this_node.get_data() == d:
				if prev_node is not None:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node.get_next()
				self.size -= 1
				return True     # data removed
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		return False  # data not found

	def find (self, d):
		# find a node with data d
		this_node = self.root
		while this_node is not None:
			if this_node.get_data() == d:
				return d
			elif this_node.get_next() == None:
				return False
			else:
				this_node = this_node.get_next()
				
	def print_list (self):
		print ("Print List..........")
		if self.root is None:
			return
		this_node = self.root
		print (this_node.data)
		while this_node.has_next():
			this_node = this_node.get_next()
			print ('-->', this_node.data)
			
	def sort (self):
		if self.size > 1:
			newlist = []
			current = self.root
			newlist.append(self.root)
			while current.has_next():
				current = current.get_next()
				newlist.append(current)
			newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True)
			newll = LinkedList()
			for node in newlist:
				newll.add_node(node)
			return newll
		return self
		
if __name__ == '__main__':
	myList = LinkedList()
	myList.add(5)
	myList.add(9)
	myList.add(3)
	myList.add(8)
	myList.add(9)
	print("size="+str(myList.get_size()))
	myList.print_list()
	myList = myList.sort()
	myList.print_list()
	myList.remove(8)
	print("size="+str(myList.get_size()))
	print("Remove 15", myList.remove(15))
	print("size="+str(myList.get_size()))
	print("Find 25", myList.find(25))
	myList.print_list()