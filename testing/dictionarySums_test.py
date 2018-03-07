import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import dictionarySums

class DictionarySumsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(dictionarySums.dictionary_sums({'I': 1.0, 'Love': 5.0, 'Python': 2.5, 'Java': 3.2}, ['I', 'Love', 'Java']), 9.2)

    def test2(self):
        self.assertEqual(dictionarySums.dictionary_sums({}, []),0.0)

    def test3(self):
        self.assertEqual(dictionarySums.dictionary_sums({'Grace': 1.7, 'Hopper': 4.5, 'Ada': 1.1, 'Lovelace': 7.2}, ['Grace', 'Hopper']), 6.2)


if __name__ == '__main__':
    unittest.main()