import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import swapTwo

class swapTwoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(swapTwo.swap_two(['one', 'two']), ['two', 'one'])

    def test2(self):
        self.assertEqual(swapTwo.swap_two([1, 2]), [2, 1])

    def test2(self):
        self.assertEqual(swapTwo.swap_two(['world', 'hello']), ['hello', 'world'])


if __name__ == '__main__':
    unittest.main()
