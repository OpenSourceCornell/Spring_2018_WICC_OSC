import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import gries

class griesTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(gries.gries(1985), 33)
    
    def test2(self):
        self.assertEqual(gries.gries(2017), 1)
    
    def test3(self):
        self.assertEqual(gries.gries(5), 2013)

if __name__ == '__main__':
    unittest.main()