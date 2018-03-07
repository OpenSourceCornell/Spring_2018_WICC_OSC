import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import countOnes

class countOnesTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(countOnes.countOnes([1,2,3]), 1)

	def test2(self):
		self.assertEqual(countOnes.countOnes([1,1,1]), 3)

	def test3(self):
		self.assertEqual(countOnes.countOnes([9,8]), 0)

	def test4(self):
		self.assertEqual(countOnes.countOnes([]), 0)


if __name__ == '__main__':
	unittest.main()