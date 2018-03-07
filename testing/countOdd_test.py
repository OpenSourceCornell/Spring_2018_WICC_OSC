import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import countOdd

class countOddTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(countOdd.count_odd([1, 2, 3, 4, 5, 6]), 3)

    def test2(self):
        self.assertEqual(countOdd.count_odd([8, 2, 2, 4, 2, 2]), 0)

    def test2(self):
        self.assertEqual(countOdd.count_odd([1, 5, 3, 1, 5, 7]), 6)


if __name__ == '__main__':
    unittest.main()
