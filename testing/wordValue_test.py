import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import wordValue

class wordValueTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(wordValue.word_value({'b': 3}, 'bb'), 6)

    def test2(self):
        self.assertEqual(wordValue.word_value({'a': 7}, 'a'), 7)

    def test2(self):
        self.assertEqual(wordValue.word_value({'a': 3, 'n': 2, 'd': 1}, 'and'), 6)


if __name__ == '__main__':
    unittest.main()
