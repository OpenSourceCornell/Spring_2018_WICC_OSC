import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import python

class pythonTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(python.python("I'm a pretty hot computer scientist"), True)
    
    def test2(self):
        self.assertEqual(python.python("java"), False)
    
    def test3(self):
        self.assertEqual(python.python("pytho?"), False)

if __name__ == '__main__':
    unittest.main()
