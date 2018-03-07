import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import sleep

class sleepTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(sleep.sleep([5, 23, 15, 17, 19]), 8.2)
    
    def test2(self):
        self.assertEqual(sleep.sleep([24, 24, 24, 24, 24, 24, 24]), 0)
    
    def test3(self):
        self.assertEqual(sleep.sleep([23, 16, 9, 3, 2, 14, 17]), 12)

if __name__ == '__main__':
    unittest.main()