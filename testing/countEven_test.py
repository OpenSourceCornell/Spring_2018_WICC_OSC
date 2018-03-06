import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import countEven

class countEvenTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(countEven.count_even([1, 2, 3, 4, 5, 6]), 3)

    def test2(self):
        self.assertEqual(countEven.count_even([8, 2, 2, 4, 2, 2]), 6)

    def test2(self):
        self.assertEqual(countEven.count_even([1, 5, 3, 1, 5, 7]), 0)


if __name__ == '__main__':
    unittest.main()
