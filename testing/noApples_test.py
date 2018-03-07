import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import noApples

class NoApplesTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(noApples.no_apples(['apple', 'Apple', 'I<3apple', 'banana', 'Microsoft']), ['Apple','banana','Microsoft'])

    def test2(self):
        self.assertEqual(noApples.no_apples([]),[])

    def test3(self):
        self.assertEqual(noApples.no_apples(['appleappleapple']), [])

    def test3(self):
        self.assertEqual(noApples.no_apples(['banana']), ['banana'])


if __name__ == '__main__':
    unittest.main()