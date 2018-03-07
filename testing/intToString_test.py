import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import intToString

class intToStringTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(intToString.intToString(2), '2')

	def test2(self):
		self.assertEqual(intToString.intToString(-4), '-4')

	def test3(self):
		self.assertEqual(intToString.intToString(0), '0')


if __name__ == '__main__':
	unittest.main()