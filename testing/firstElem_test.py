import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import firstElem

class firstElemTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(firstElem.firstElem([1,2,3]), 1)

	def test2(self):
		self.assertEqual(firstElem.firstElem([-4]), -4)

	def test3(self):
		self.assertEqual(firstElem.firstElem([9]), 9)

	def test4(self):
		self.assertEqual(firstElem.firstElem([]), None)


if __name__ == '__main__':
	unittest.main()