import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import GriesVs

class GriesVsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(GriesVs.Gries_vs(56), False)

    def test2(self):
        self.assertEqual(GriesVs.Gries_vs(57), True)

    def test2(self):
        self.assertEqual(GriesVs.Gries_vs(2), False)


if __name__ == '__main__':
    unittest.main()
