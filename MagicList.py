class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		if len(M)==1 :
			return None
		else:
			return M[1]
	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		# print("Insert called on ", E)
		if len(M)==1:
			M.append(E)
			self.data = M
			return M
		M.append(E)
		indexAdded = len(M)-1
		parentIndex = int(indexAdded/2)
		while M[parentIndex]>=M[indexAdded] and indexAdded != 1 and parentIndex!= 0 :
			temp = M[parentIndex]
			M[parentIndex] = M[indexAdded]
			M[indexAdded] = temp
			indexAdded = parentIndex
			parentIndex = int(indexAdded/2)
		self.data = M
		return M
	
	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
		if len(M)==1:
			return M
		# Bring Last Element to root
		M[1]=M[len(M)-1]
		# Delete Last element
		M = M[:-1]

		currentHole = 1
		child1 = 2*currentHole
		child2 = 2*currentHole + 1
		while True :
			if child1>(len(M)-1) :
				# No Children Exist
				self.data = M
				return M
			elif child2<=(len(M)-1):
				# Both Children Exist
				if M[child1]>=M[currentHole] and M[child2]>=M[currentHole] :
					#Both children are bigger then stop
					self.data = M
					return M
				else:
					smallerChildIndex = None
					if M[child1]<M[child2] :
						smallerChildIndex = child1
					else:
						smallerChildIndex = child2
					temp = M[smallerChildIndex]
					M[smallerChildIndex]=M[currentHole]
					M[currentHole] = temp
					currentHole = smallerChildIndex
					child1 = 2*currentHole
					child2 = 2*currentHole + 1
			else:
				# Just 1 child1 exists
				if M[child1]>=M[currentHole] :
					# Nothing Needed
					self.data = M
					return M
				else:
					smallerChildIndex = child1
					temp = M[smallerChildIndex]
					M[smallerChildIndex]=M[currentHole]
					M[currentHole] = temp
					currentHole = smallerChildIndex
					child1 = 2*currentHole
					child2 = 2*currentHole + 1

		self.data = M
		return M
	#defining a function to print the magic list
	def __str__(self):
		M = self.data
		N = [str(i) for i in M]
		result = ' '.join(N)
		return result

def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	# Convert a list L to Magic List M
	M = MagicList ()
	for i in L:
		M.insert(i)
	answer = 0
	for z in range(K):
		answer+=M.findMin()
		M.deleteMin()
	return answer
	
	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)
	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 4 :
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	print(x)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")


###################My test cases ##############################
##Test1 
L = MagicList()
L.insert(3)
L.insert(13)
print(L)
L.insert(2)
L.insert(11)
print(L)
L.insert(4)
L.insert(1)
print(L)
L.insert(2)
L.deleteMin()
print(L)
L.deleteMin()
L.deleteMin()
print(L)
#Test2
A = [0,1,2,1,2,1,2,1,3,4,2,4,2,4,2,4,5,3,2,2,1,1,0,0]
print(K_sum(A,3)) # output should be 0
print(K_sum(A,6)) #output should be 3
print(K_sum(A,9)) #output should be 6


