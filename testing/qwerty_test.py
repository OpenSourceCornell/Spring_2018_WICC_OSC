import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import qwerty

class pythonTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(qwerty.qwerty("eakce ipc.o co mf d.pr"), "david gries is my hero")
    
    def test2(self):
        self.assertEqual(qwerty.qwerty("c nrk. rl.b orgpj."), "i love open source")
    
    def test3(self):
        self.assertEqual(qwerty.qwerty("lc .'gano ydp..", "pi equals three")

if __name__ == '__main__':
    unittest.main()