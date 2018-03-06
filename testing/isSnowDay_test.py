import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import isSnowDay

class isSnowDayTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(isSnowDay.is_snow_day([0, 2, 3, 4]), [False, False, False, True])

    def test2(self):
        self.assertEqual(isSnowDay.is_snow_day([99, 99, 4, 4]), [False, False, True, True])

    def test2(self):
        self.assertEqual(isSnowDay.is_snow_day([0, 2, 3, 2]), [False, False, False, False])


if __name__ == '__main__':
    unittest.main()
