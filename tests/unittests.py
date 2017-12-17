import unittest
from list_2 import list_2
from random import randint

class Testing_list_2_modules(unittest.TestCase):
	"""
	docstring for Testing_list_2_modules.

	This Class is used for testing each method of list_2
	There are, however, a few methods that are skipped for this testing
	These are addressed in the documentation for list_2 and are listed as follows:
		1. __lt__
		2. __gt__
		3. __le__
		4. __ge__
		5. __repr__
	"""

	def setUp(self):

		self.l=list(range(100))
		self.l2=list(range(100))

	def test_list_2_init(self):

		self.assertEqual(self.l, self.l2)

	def test_list_2_append(self):

		self.l.append(10)
		self.l2.append(10)

		self.assertEqual(self.l, self.l2)

	def test_list_2_pop(self):

		self.l.pop()
		self.l2.pop()

		self.assertEqual(self.l, self.l2)

		self.l.pop(3)
		self.l2.pop(3)

		self.assertEqual(self.l, self.l2)

		self.l.pop(-3)
		self.l2.pop(-3)

		self.assertEqual(self.l, self.l2)

	def test_list_2_clear(self):

		self.l.clear()
		self.l2.clear()

		self.assertEqual(self.l, self.l2)

	def test_list_2_copy(self):

		l3=self.l.copy()
		l4=self.l2.copy()

		self.assertEqual(l3, l4)

	def test_list_2_count(self):

		self.l=[]

		for x in range(10):
			self.l.append(randint(0, 10))

		self.l2=list_2(self.l)

		self.assertEqual(self.l.count(5), self.l2.count(5))

	def test_list_2_extend(self):

		l3=[ randint(0, 10) for i in range(100) ]

		self.l.extend(l3)
		self.l2.extend(l3)

		self.assertEqual(self.l, self.l2)

	def test_list_2_index(self):

		n1=self.l.index(4)
		n2=self.l2.index(4)

		self.assertEqual(n1, n2)

	def test_list_2_remove(self):

		self.l.remove(55)
		self.l2.remove(55)

		self.assertEqual(self.l, self.l2)

	def test_list_2_reverse(self):

		self.l.reverse()
		self.l2.reverse()

		self.assertEqual(self.l, self.l2)

	def test_list_2_sort(self):

		self.l=[randint(0, 100) for x in range(100)]
		self.l2=list_2(self.l)

		self.l.sort()
		self.l2.sort()

		self.assertEqual(self.l, self.l2)

	def test_list_2_contains(self):

		t1= [x in self.l for x in self.l]
		t2= [x in self.l2 for x in self.l2]

		self.assertEqual(t1, t2)

	def test_list_2_del(self):

		n=randint(0, len(self.l))

		del self.l[n]
		del self.l2[n]

		self.assertEqual(self.l, self.l2)

	def test_list_2_getitem(self):

		n=randint(0, len(self.l))

		self.assertEqual(self.l[n], self.l2[n])

	def test_list_2_iadd(self):

		self.l+=[4, 5]
		self.l2+=[4, 5]

		self.assertEqual(self.l, self.l2)

	def test_list_2_imul(self):

		self.l*=3
		self.l2*=3

		self.assertEqual(self.l, self.l2)

	def test_list_2_iter(self):

		l3=[]
		l4=[]

		for x in self.l:
			l3.append(x)

		for i in self.l2:
			l4.append(i)

		self.assertEqual(l3, l4)

	def test_list_2_len(self):

		len_1=len(self.l)
		len_2=len(self.l2)

		self.assertEqual(len_1, len_2)

	def test_list_2_setitem(self):

		n=randint(0, len(self.l))

		self.l[n]=42
		self.l2[n]=42

		self.assertEqual(self.l, self.l2)

	def test_list_2_str(self):

		self.assertEqual(str(self.l), str(self.l2))

	def test_list_2_add(self):
		l3=[randint(0, 100) for i in range(100)]

		self.l = self.l + l3
		self.l2 = self.l2 + l3

		self.assertEqual(self.l, self.l2)

	def test_list_2_iadd(self):
		l3=[randint(0, 100) for i in range(100)]

		self.l+=l3
		self.l2+=l3

		self.assertEqual(self.l, self.l2)

	def test_list_2_eq(self):
		l3_1=list(self.l)
		l3_2=list_2(self.l2)

		self.assertTrue(self.l==l3_1)
		self.assertTrue(self.l2==l3_2)

		self.assertEqual(self.l, self.l2)

	def test_list_2_reversed(self):
		self.l.reverse()
		self.l2.reverse()

		self.assertEqual(self.l, self.l2)

unittest.main()