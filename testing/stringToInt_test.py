import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import stringToInt

class stringToIntTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(stringToInt.stringToInt('2'), 2)

	def test2(self):
		self.assertEqual(stringToInt.stringToInt('-4'), -4)

	def test3(self):
		self.assertEqual(stringToInt.stringToInt('0'), 0)


if __name__ == '__main__':
	unittest.main()