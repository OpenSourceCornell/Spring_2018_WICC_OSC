import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import calcSum

class calcSumTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(calcSum.calc_sum([0, 1, 0, 1]), 2)

    def test2(self):
        self.assertEqual(calcSum.calc_sum([2, 2, 2, 2]), 8)

    def test2(self):
        self.assertEqual(calcSum.calc_sum([-1, 1, -3, 3]), 0)


if __name__ == '__main__':
    unittest.main()
