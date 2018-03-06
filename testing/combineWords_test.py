import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import combineWords

class combineWordsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(combineWords.combine_words(['git','merge']), 'git merge')

    def test2(self):
        self.assertEqual(combineWords.combine_words(['Gates', 'Hall']), 'Gates Hall')

    def test2(self):
        self.assertEqual(combineWords.combine_words(['a', 'b']), 'a b')


if __name__ == '__main__':
    unittest.main()
