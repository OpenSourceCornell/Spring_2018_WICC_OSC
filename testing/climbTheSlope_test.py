import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import climbTheSlope

class ClimbSlopeTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(climbTheSlope.climb_the_slope(0.0, 5.0), 0.0)

    def test2(self):
        self.assertEqual(round(climbTheSlope.climb_the_slope(35.2, 0.37),1), 95.1)

    def test3(self):
        self.assertEqual(climbTheSlope.climb_the_slope(1.0, 0.5), 2.0)


if __name__ == '__main__':
    unittest.main()