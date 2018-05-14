#!/bin/python

class BSTree:
	''' Note: keys appear at most one time in this tree '''
	def __init__(self):
		self._tree=BSTreeNull()

	def delete(self, key):
		self._tree=self._tree.delete(key)

	def insert(self, key):
		self._tree=self._tree.insert(key)

	def is_empty(self):
		return(self._tree.is_empty())

	def print_inorder(self):
		self._tree.print_inorder()

	def print_preorder(self):
		self._tree.print_preorder()

	def print_postorder(self):
		self._tree.print_postorder()

	def get_max(self):
		return self._tree.get_max()

	def get_min(self):
		return self._tree.get_min()

	def find(self, key):
		''' return whether key is in this tree '''
		return self._tree.find(key)

	def range(self, lower, upper):
		''' return a list of all keys in self between lower (inclusive)  and upper (exclusive)'''
		if lower<upper:
			return self._tree.range(lower, upper)
		else:
			return []
	def height(self):
		
		return self._tree.height()

	def __str__(self):
		return str(self._tree)

class BSTreeNode:
	
	def __init__(self, key):
		self._left=BSTreeNull()
		self._right=BSTreeNull()
		self._key=key
	def height(self):
		left = self._left.height()
		right = self._right.height()
		bigger = max(left,right)
		return bigger + 1
	

	def delete(self, key):
		if key<self._key:
			self._left=self._left.delete(key)
			return self
		if key>self._key:
			self._right=self._right.delete(key)
			return self
		# key == self._key
		if self._left.is_null() and self._right.is_null():
			return self._left # any BSTreeNull will do

		if self._left.is_null():
			return self._right

		if self._right.is_null():
			return self._left

		m=self._left.get_max()
		self._key=m._key
		self._left=self._left.delete(self._key)
		return self
		
	def print_postorder(self):
		self._left.print_postorder()
		self._right.print_postorder()
		print(str(self._key)+ " " )
		return 

	def print_preorder(self):
		print(str(self._key)+ " " )
		self._left.print_preorder()
		self._right.print_preorder()
		return 

	def print_inorder(self):
		self._left.print_inorder()
		print(str(self._key)+ " " )
		self._right.print_inorder()
		return 

	def get_min(self):
		m=self._left.get_min()
		if m.is_null():
			return self
		else:
			return m

	def get_max(self):
		m=self._right.get_max()
		if m.is_null():
			return self
		else:
			return m

	def is_null(self):
		return False

	def insert(self, key):
		''' 
		insert key in my subtree if not already there, 
		return the root of my subtree
		'''
		if key<self._key:
			self._left=self._left.insert(key)
		elif key>self._key:
			self._right=self._right.insert(key)
		else:
			 pass
		return self

	def find(self, key):
		''' return whether key is in this subtree '''
		if key<self._key:
			return self._left.find(key)
		elif self._key<key:
			return self._right.find(key)
		else: # self._key=key
			return True

	def range(self, lower, upper):
		''' return a list of all keys in this subtree 
		between lower (inclusive)  and upper (exclusive)'''

		if self._key<=lower:
			left=[]
		else:
			left=self._left.range(lower, upper)

		if lower<=self._key and self._key<upper:
			middle=[self._key]
		else:
			middle=[]

		if upper<self._key:
			right=[]
		else:
			right=self._right.range(lower, upper)

		return left+middle+right

	def __str__(self):
		return str(self._left)+" "+str(self._key)+" "+str(self._right)

	def is_empty(self):
		return False

class BSTreeNull:
	def __init__(self):
		pass
	def height(self):
		return 0 

	def delete(self, key):
		return self

	def is_empty(self):
		return True

	def is_null(self):
		return True

	def get_max(self):
		return self

	def get_min(self):
		return self

	def print_inorder(self):
		return 

	def print_preorder(self):
		return 

	def print_postorder(self):
		return 

	def insert(self, key):
		''' 
		insert key in my subtree if not already there, 
		return the root of my subtree
		'''
		return BSTreeNode(key)

	def find(self, key):
		return False

	def range(self, lower, upper):
		''' return a list of all keys in this subtree 
		between lower (inclusive)  and upper (exclusive)'''
		return []

	def __str__(self):
		return ""


if __name__ == '__main__':
	t=BSTree()
	print(t.is_empty())
	
	t=BSTree()
	for v in [65, 2, 99, 22, 132, 5, 22, 6]:
		t.insert(v)
		print("after t.insert("+str(v)+") str(t)="+str(t))

	for v in [22, 44, 65, 22,7,2, 1, 99, 102, 132, 5, 6, 22, 159]:
		print("t.find(",v,")=",t.find(v))

	 # 2  5  6  22  65  99  132 
	for (lower, upper) in [(-5, 200), (-5, 100), (3, 200), (6, 99), (22, 22), (22, 23), (15, 7)]:
		print("t.range(",lower,",",upper,")=", t.range(lower, upper))

	for v in [22, 44, 65, 7,2,  22, 99, 102, 132, 5, 6]:
		t.delete(v)
		print("after t.delete(",v,") str(t)="+str(t))

