import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import alternatingLists

class AlternatingListsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(alternatingLists.alternating_lists(['a','b','c','d'], [1,2]), ['a',1,'b',2,'c','d'])

    def test2(self):
        self.assertEqual(alternatingLists.alternating_lists([], []), [])

    def test3(self):
        self.assertEqual(alternatingLists.alternating_lists([],['a','b','c']), ['a','b','c'])


if __name__ == '__main__':
    unittest.main()