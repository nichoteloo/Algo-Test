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
				p = p.link
			print()