import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import returnBiggerString

class returnBiggerStringTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(returnBiggerString.bigger_string('duffield', 'upson'), 'duffield')

    def test2(self):
        self.assertEqual(returnBiggerString.bigger_string('rpcc', 'appel'), 'appel')

    def test2(self):
        self.assertEqual(returnBiggerString.bigger_string('aa', 'a'), 'aa')


if __name__ == '__main__':
    unittest.main()
