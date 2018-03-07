import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import square

class squareTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(square.square(2), 4)

	def test2(self):
		self.assertEqual(square.square(-4), 16)

	def test3(self):
		self.assertEqual(square.square(0), 0)

	def test4(self):
		self.assertEqual(square.square(1), 1)


if __name__ == '__main__':
	unittest.main()