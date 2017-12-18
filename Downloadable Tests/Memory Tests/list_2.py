from numpy import array, arange

class list_2:

	"""
	list_2() -> new empty list
	list_2(iterable) -> new list initialized from iterable's items
	"""

	def __init__(self, iterable = [], dtype=object):

		#Checking if object is iterable
		try:
			for x in iterable:

				break

		#Raises relevant error when object isn't iterable
		#If the object isn't iterable, then the object can't be made into a list
		except Exception as e:
			raise e

		#Creating a flexible array
		#Setting dtype to base class ('object') to ensure that
		#any object can be imported/used

		#IMPORTANT NOTE: USING OBJECT CLASS DECREASES MEMORY EFFICIENCY GREATLY!!!
		#IF MEMORY EFFICIENCY IS BIGGEST CONCERN, CHANGE DATA TYPE TO AN
		#INTEGER OR FLOAT OR WHATEVER IS GOING TO BE PRIMARILY USED
		#This is maybe to be implemented in an upcoming version
		self.arr = arange(len(iterable), dtype=dtype) if len(iterable) else array([])

		#This block of code is used to transfer iterable's elements from
		#container to an array

		#Fr, this block of code can be improved.
		#More importantly, dumbass author should re-write this section of code to make
		#sure that everything is up to standard based on PyPI recommendations
		try:
			#Strings have an issue where need to be iterated with a for loop
			#as compared to default method (mentioned below)
			if isinstance(iterable, str):
				for x in range(len(iterable)):
					self.arr[x]=iterable[x]

			#Dictionaries are also a special case and is taken care of by following steps
			elif isinstance(iterable, dict):
				i=0
				for x in iterable:
					self.arr[i]=x
					i+=1

			#Default way of transferring all items in data-type to given array
			else:
				self.arr[:]=iterable[:]

		except Exception as e:
			raise e

	def __str__(self):

		#This code can be re-written in a better way

		#It essentially converts array to a list and returns str of list
		#This part can be re-written as: s='[' + <each element separated with a comma and space> + ']'
		return str(list(self.arr))

	def __add__(self, y):

		"""
		Return self+value
		"""

		#If condition checks if addition is possible
		#Conditions, when addition between a list fails, are (by nature of lists)
		#   When y is a datatype which is not a list or list_2 object

		#This if condition runs when item is of type: list or an object of list_2
		if isinstance(y, list) or type(y)==type(self):
			temp_arr=arange( len(self) + len(y) , dtype=object) #Creating an empty array of length=len(self)+len(y)
													   #This empty array is large enough to hold all values of self and object y

			#Next two steps are worked with indexing
			#Indexing is used in this instance for FASTER PERFORMANCE and BETTER MEMORY ALLOCATION
			#If a better method is found which is better somehow, n it is recommended that that method is used
			temp_arr[:len(self)]=self[:] #Transfering a copy of self to first part of array
			temp_arr[len(self):]=y[:]	#Transfering a copy of y to latter part of array

			return list_2(temp_arr) #Returning a list_2 object

		#This is situation where an error is to be raised
		#An error is to be raised whenever y is not a list, array or list_2 object
		#You can check error by typing: [<list object stuff>] + <object that is not a list, or list_2 object>
		#Error would be: TypeError: can only concatenate list (not <object that is not a list, or list_2 object>) to list
		else:
			type_val=str(type(y)) #Getting string of type of y so it's easier to use later
			type_name=type_val[type_val.find("'") + 1 : type_val.find("'", type_val.find("'") + 1 )] #Isolating type name from type_val
			raise TypeError('can only concatenate list (not "{0}") to list'.format(type_name)) #Raising appropriate TypeError based on

	def __iadd__(self, value):

		"""
		Implement self+=value.
		"""

		#Be sure to add a check to ensure that we can add value to list
		#Check to ensure that thing can be iterated through
		#Similar steps compared to what __add__ function does
		temp_lst=arange(len(self)+len(value), dtype=self.arr.dtype) #Creating an empty array of length=len(self)+len(y)

		temp_lst[:len(self)]=self[:]  #Transfering a copy of self to first part of array
		temp_lst[len(self):]=value[:] #Transfering a copy of y to latter part of array

		self.arr=arange(len(self)+len(value), dtype=self.arr.dtype) #Making self.arr an empty array of length=len(self)+len(y)
		self.arr[:]=temp_lst[:]					 #Transfering a copy longer array to self

		return self

	def __delitem__(self, index): #Changes to be made: needs to be able to include slices

		"""
		Delete self[key]
		"""

		if isinstance(index, slice): #Code flow to follow if index was given is a slice and not an integer

			#Find each index and replace that position with an identification string (in this case, identification string = '123456787654321')
			#And assign a copy to self
			self[:] = list_2([(self[x] if (x not in range(len(self))[index] ) else '123456787654321') for x in range(len(self))])[:]

			#Running a loop total number of times identification string has been written in self
			for x in range(self.count('123456787654321')):
				self.remove('123456787654321') #Removing instance of identification string from self
											   #This removes all elements in array which are
											   #the same as the identification string

		elif isinstance(index, int): #Checking to ensure that index is an integer
			self[:] = list_2(self[:index])+list_2(self[index+1:]) #Setting entire array to include everything but selected index

		else:
			#Raising TypeError when we find that index is not an integer or slice
			raise TypeError('list indices must be integers or slices, not {0}'.format(type(index)))

	def __repr__(self):

		"""
		Return repr(self).
		"""

		#Function used to represent class when called from IDLE
		#For example, after importing, type list_2(range(10)) in IDLE, and this is what is returned
		#Similar to string function, this code can be re-written in a better way

			#It essentially converts array to a list and returns str of list
			#This part can be re-written as: s='[' + <each element separated with a comma and space> + ']'

		return (str(list(self.arr)))

	def __len__(self): #Returns length of list_2 object

		"""
		Return len(self).
		"""

		# if type(None) == type(self.arr): Checks if it is an empty list, and then return 0
		# 	return 0

		# else:
		# 	return len(self.arr) Otherwise, returns length of array with len function
		# 						 Author believes that this can be speeded up more by using arrays and indexing
		return len(self.arr)

	def __getitem__(self, index):

		"""
		x.__getitem__(y) <==> x[y]
		"""

		return self.arr[index] #Returns the item at given index, and raises error otherwise

	def __setitem__(self, key, value):

		"""
		Set self[key] to value.
		"""

		if isinstance(key, slice): #Checking if a slice has been passed
			keys=self[key.start:key.stop:key.step] #Getting items at its proper position
			self.arr=arange(len(value)) #Creating an empty array
			self.arr[:]=value[:] #Assigning all the values to self

		else:
			if key <= len(self) or 0 > key > len(self):	#If key is in range of self, then it sets value to its proper position in the array
				self.arr[key] = value
			else:
				raise IndexError("list index out of range") #If key is in

	def __contains__(self, value):

		"""
		Return key in self.
		"""

		return (value in self.arr) #returns if a value is in the list_2 object

	def __iter__(self): #Generator function to return each element

		"""
		Implement iter(self).
		"""

		for x in self.arr:
			yield(x)

	def __reversed__(self): #Generator function to return each element from reverse

		"""
		L.__reversed__() -- return a reverse iterator over the list
		"""

		for x in reversed(self.arr):
			yield(x)

	def __eq__(self, value): #Equality operator to check if 2 items are equal, irrelevant of value's type

		"""
		Return self==value.
		"""

		if len(self) != len(value): #Checking if the length of the two items is equal
			return False

		else:
			for x in range(len(self)):
				if self[x] != value[x]: #Checking if each element is the same in the two operators or not
					return False #If for any element they're not equal, it returns false
			else:
				return True #If it passes all checks before it, it is understood that the two objects are equal

	def __lt__(self, value):

		"""
		return self<value
		"""

		raise NameError("This feature has not been implimented yet")

	def __gt__(self, value):

		"""
		return self>value
		"""

		raise NameError("This feature has not been implimented yet")

	def __ge__(self, value):

		"""
		return self>=value
		"""

		raise NameError("This feature has not been implimented yet")

	def __le__(self, value):

		"""
		return self<=value
		"""

		raise NameError("This feature has not been implimented yet")


	def __mul__(self, mul_value): #Multiplication function in lists

		"""
		Return self*value.n
		"""

		temp_lst=arange(len(self)*mul_value, dtype=self.arr.dtype) #Creating a placeholder array of the appropriate size
		for x in range(mul_value): #Adding the elements of that array the total number of times that we have to repeat the list
			temp_lst[len(self)*x:len(self)*(x+1)]=self[:] #Assigning a copy of the self to the correct positions
		return list_2(temp_lst) #Returning a list_2 object which meets our specifications

	def __imul__(self, mul_value): #implementing multiplication function in list_2

		"""
		Implement self*=value.
		"""

		temp_lst=arange(len(self)*mul_value, dtype=self.arr.dtype) #Creating a placeholder array of the appropriate size
		for x in range(mul_value): #Adding the elements of that array the total number of times that we have to repeat the list
			temp_lst[len(self)*x:len(self)*(x+1)]=self[:] #Assigning a copy of the self to the correct positions
		return list_2(temp_lst) #Returning a list_2 object which meets our specifications

	def append(self, item): #Append function in list_2

		"""
		L.append(object) -> None -- append object to end
		"""

		temp_arr=arange(len(self) + 1) #creating an empty array
		temp_arr[:len(self)] = self.arr[:] #assigning a copy of self to the first half of the temp array
		temp_arr[len(self)] = item	#assigning the item to the last position of the array
		self.arr = temp_arr	#assigning the entire temp array to self.arr

	def pop(self, index = -1): #Pop function in list_2, default parameter is -1

		"""
		L.pop([index]) -> item -- remove and return item at index (default last).
		Raises IndexError if list is empty or index is out of range.
		"""

		if index<0: #Converting the negative index to the positive index
			index=index+len(self)
		temp_val=self[index] #collecting the item at index's position to return later
		self[:]=list_2(self[:index])+list_2(self[index+1:]) #Making the list_2 smaller with help of indexing
		return temp_val #returning the item

	def remove(self, value): #remove function in list_2

		"""
		L.remove(value) -> None -- remove first occurrence of value.
		Raises ValueError if the value is not present.
		"""

		for x in range(len(self)):
			if self [x] == value: #Finding the first instance in the list
				self.pop(x)	#Removing that value
				break #Quitting the loop cuz we found it
		else:
			raise ValueError("list.remove(x): {0} not in list".format(value)) #Printing the error message when we couldn't find the item in the list

	def count(self, value): #Count function in list_2

		"""
		L.count(value) -> integer -- return number of occurrences of value
		"""

		val_count = 0	#number of times the value found is 0
		for x in self: #Counting the number of times the item has been found in the list
			if x == value:
				val_count += 1
		return val_count #returning the number of times the value has occurred

	def clear(self): #clear function in list_2

		"""
		L.clear() -> None -- remove all items from L
		"""

		self.arr = arange(0, dtype=object) #sets the array to an empty array of dtype object

	def reverse(self): #reverse function in list_2

		"""
		L.reverse() -- reverse *IN PLACE*
		"""

		self[:]=self[::-1] #sets self.arr to its reverse

	def index(self, value, start = None, stop = None): #index function in list_2

		"""
		L.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		"""

		if start == None: start = 0 #If start is None, it's set to 0
		if stop == None: stop = len(self) #if stop is None, it's set to len(self)
		temp_lst = self[start:stop]	#creating a copy of the list
		for x in range(len(temp_lst)):
			if temp_lst[x] == value: #finding the value in the list
				return x+start #returning the position in the copy of the list as well as the starting position
		else:
			raise ValueError('{0} not in list'.format(value)) #raising an error when we can't find the value

	def extend(self, iterable): #extend function in list_2

		"""
		L.extend(iterable) -> None -- extend list by appending elements from the iterable
		"""

		self+=list_2(iterable) #adding the second iterable to self.arr after converting it to a list_2 object

	def insert(self, index, item): #insert function in list_2

		"""
		L.insert(index, object) -- insert object before index
		"""

		self[:] = list_2(self[:index])+list_2(arange(1))+list_2(self[index:]) #increasing the size of self at position: index
		self[index]=item #assigning the item at the index

	def sort(self):

		"""
		L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
		"""

		#sort function in list_2
		#implementing selection sort to the list_2 object
		for i in range(0, len(self)):
			min_pos=i
			for j in range(i, len(self)):
				if self[min_pos] > self[j]:
					min_pos=j
			self[min_pos], self[i]=self[i], self[min_pos]

	def copy(self): #copy function in list_2

		"""
		L.copy() -> list -- a shallow copy of L
		"""

		return list_2(self.arr) #returning a copy of self.arr

def main():
	for i in dir(list_2):
		help(eval('list_2.'+i))

if __name__ == '__main__':
	main()
