import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import sumRange

class sumRangeTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(sumRange.sumRange(4), 10)

	def test2(self):
		self.assertEqual(sumRange.sumRange(1), 1)

	def test3(self):
		self.assertEqual(sumRange.sumRange(15), 120)


if __name__ == '__main__':
	unittest.main()