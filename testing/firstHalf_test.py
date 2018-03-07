import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import firstHalf

class firstHalfTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(firstHalf.first_half('abcdef'), 'abc')

    def test2(self):
        self.assertEqual(firstHalf.first_half('abcde'), 'ab')

    def test2(self):
        self.assertEqual(firstHalf.first_half('firsthalf'), 'firs')


if __name__ == '__main__':
    unittest.main()
