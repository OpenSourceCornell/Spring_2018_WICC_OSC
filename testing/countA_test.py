import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import countA

class countATest(unittest.TestCase):
    def test1(self):
        self.assertEqual(countA.count_a('aabbcc'), 2)

    def test2(self):
        self.assertEqual(countA.count_a('aaabcc'), 3)

    def test2(self):
        self.assertEqual(countA.count_a('bbbcc'), 0)


if __name__ == '__main__':
    unittest.main()
