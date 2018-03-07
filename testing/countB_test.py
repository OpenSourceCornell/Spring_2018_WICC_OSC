import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import countB

class countBTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(countB.count_b('aabbcc'), 2)

    def test2(self):
        self.assertEqual(countB.count_b('aabbbb'), 4)

    def test2(self):
        self.assertEqual(countB.count_b('aabcc'), 1)


if __name__ == '__main__':
    unittest.main()
