from double_linked_list import DoubleLinkedList

def main():
	dll = DoubleLinkedList('b')
	dll.print_all() # b

	dll.delete_at_index(0)
	dll.print_all() # []

	dll.insert_at_index('a',0)
	dll.insert_at_index('c',2)
	dll.insert_at_end('d')
	dll.insert_at_index('x',10)
	dll.print_all() # ['a', 'c', 'd', 'x']

	for i in range(4):
		dll.print_at_index(i)
	'''
	a
	c
	d
	x
	'''

	dll.delete_at_index(0)
	dll.print_all() # ['c', 'd', 'x']

	dll.delete_at_index(2)
	dll.print_all() # ['c', 'd']

	dll.delete_at_index(5)
	dll.print_all() # ValueError: Index out of bounds: index = 5 (Zero-based indexing)

if __name__ == "__main__":
	main()