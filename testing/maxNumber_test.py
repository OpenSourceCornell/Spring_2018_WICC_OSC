import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import maxNumber

class MaxNumberTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxNumber.max_number([1,2,3,4,5]),5)

    def test2(self):
        self.assertEqual(maxNumber.max_number([]),None)

    def test3(self):
        self.assertEqual(maxNumber.max_number([5,5,5]),5)

if __name__ == '__main__':
    unittest.main()