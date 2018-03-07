import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import clockTowerSteps

class clockTowerStepsTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(clockTowerSteps.clockTowerSteps(), 161)

	def test2(self):
		self.assertEqual(clockTowerSteps.clockTowerSteps(), 161)

	def test3(self):
		self.assertEqual(clockTowerSteps.clockTowerSteps(), 161)


if __name__ == '__main__':
	unittest.main()