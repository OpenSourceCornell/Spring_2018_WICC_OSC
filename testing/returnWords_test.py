import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import returnWords

class returnWordsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(returnWords.return_words('hello world'), ['hello', 'world'])

    def test2(self):
        self.assertEqual(returnWords.return_words('Gates Hall has the best bathrooms'), ['Gates', 'Hall', 'has', 'the', 'best', 'bathrooms'])

    def test2(self):
        self.assertEqual(returnWords.return_words('a b c'), ['a', 'b', 'c'])


if __name__ == '__main__':
    unittest.main()
