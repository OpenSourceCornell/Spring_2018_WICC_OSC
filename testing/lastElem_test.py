import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import lastElem

class lastElemTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(lastElem.lastElem([1,2,3]), 3)

	def test2(self):
		self.assertEqual(lastElem.lastElem([-4]), -4)

	def test3(self):
		self.assertEqual(lastElem.lastElem([9]), 9)

	def test4(self):
		self.assertEqual(lastElem.lastElem([]), None)


if __name__ == '__main__':
	unittest.main()