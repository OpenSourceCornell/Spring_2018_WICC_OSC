import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import doubleAndTriple

class doubleAndTripleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(doubleAndTriple.double_and_triple([1, 2, 3, 8, 4, 6]), [3, 4, 9, 16, 12, 12])

    def test2(self):
        self.assertEqual(doubleAndTriple.double_and_triple([-1, -2, -3, -8, -4, -6]), [-3, -4, -9, -16, -12, -12])

    def test2(self):
        self.assertEqual(doubleAndTriple.double_and_triple([0, 0]), [0,0])


if __name__ == '__main__':
    unittest.main()
