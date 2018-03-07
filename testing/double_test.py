import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import double

class doubleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(double.double([0,1,2]),[0,2,4])

    def test2(self):
        self.assertEqual(double.double([4,4,2]),[8,8,4])

    def test2(self):
        self.assertEqual(double.double([-1,-2,-3]),[-2,-4, -6])


if __name__ == '__main__':
    unittest.main()
