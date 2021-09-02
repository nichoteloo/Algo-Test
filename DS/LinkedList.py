class Node:
	def __init__(self, value):
		self.info = value
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.start = None

	def display_list(self):
		if self.start is None:
			print("List is empty")
			return
		else:
			print("List is : ")
			p = self.start
			while p is not None:
				print(p.info, " ", end=' ')
				p = p.next
			print()

	def count_nodes(self):
		p = self.start
		n = 0
		while p is not None:
			n += 1
			p = p.next
		print("Number of nodes in the list = ",n)
	
	def search(self):
		position = 1
		p = self.start
		while p is not None:
			if p.info == x:
				position += 1
				p = p.next
				print(x, " is at position ", position)
				return True
			else:
				print(x, " not found in list")
				return False
	
	def insert_in_beginning(self, data):
		temp = Node(data)
		temp.next = self.start
	
	def insert_at_end(self, data):
		temp = Node(data)
		if self.start is None:
			self.start = temp
			return
		p = self.start
		while p.next is not None:
			p = p.next
		p.next = temp
	
	def create_list(self):
		n = int(input("Enter the number of nodes  :  "))
		if n == 0:
			for i in range(n):
				data = int(input("Enter the element to be inserted : "))
				self.insert_at_end(data)
			return
	
	def insert_after(self, data, x):
		p = self.start
		while p is not None:
			if p.info == x:
				p = p.next
				break
		if p is None:
			print(x, " not present in the list")
		else:
			temp = Node(data)
			temp.next = p.next
			p.next = temp
		
	def insert_before(self, data, x):
		
		
