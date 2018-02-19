from linked_list_node import DoubleLinkedListNode

class DoubleLinkedList:
	# An implementation of doubly linked list with zero-based indexing
	def __init__(self, val):
		self.head = DoubleLinkedListNode(val)

	def __iter__(self):
		iterator = self.head
		while iterator:
			yield iterator
			iterator = iterator.next

	def _ask_index(self, ind=None):
		while True:
			if ind == None: ind = int(raw_input('enter position at which to insert'))
			if ind < 0: print('invalid input. try again.')
			else: break
		return ind
	
	def insert_at_end(self, val=None):
		if val == None: val = raw_input('enter value of new node')
		new_node = DoubleLinkedListNode(val)
		if not self.head:
			# empty linkedlist
			self.head = new_node
			return
		iterator = self.head
		while iterator.next:
			iterator = iterator.next
		iterator.next = new_node

	def insert_at_index(self, val=None, ind=None):
		if val == None: val = raw_input('enter value of new node')
		ind = self._ask_index(ind)

		new_node = DoubleLinkedListNode(val)

		prev, iterator = None, self.head
		if ind == 0:
			self.head = new_node

		while ind > 0:
			prev = iterator
			iterator = iterator.next
			ind -= 1
			if not iterator: 
				print('Index out of bounds, so appending to end of LinkedList.')
				break
		new_node.prev = prev
		new_node.next = iterator
		if prev:
			new_node.prev.next = new_node
		if iterator:
			new_node.next.prev = new_node

	def print_all(self):
		print([node.val for node in self])

	def print_at_index(self, ind=None):
		ind = self._ask_index(ind)
		temp = ind

		iterator = self.head
		while ind > 0:
			iterator = iterator.next
			ind -= 1
		if not iterator: raise IndexError('Index out of bounds: index = {} (Zero-based indexing)'.format(temp))
		print(iterator.val)

	def delete_at_index(self, ind=None):
		if not self.head:
			raise IndexError('Trying to remove from empty LinkedList')

		ind = self._ask_index(ind)
		temp = ind

		if ind == 0: 
			self.head = self.head.next
			return

		prev, iterator = None, self.head
		while ind > 0:
			prev = iterator
			iterator = iterator.next
			if not iterator:
				raise ValueError('Index out of bounds: index = {} (Zero-based indexing)'.format(temp))
			ind -= 1

		if iterator.next:
			iterator.next.prev = prev
		if prev:
			prev.next = iterator.next

