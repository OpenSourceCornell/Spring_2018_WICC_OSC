import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import bananaGrams

class bananaGramsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(bananaGrams.banana_grams('banana'), True)

    def test2(self):
        self.assertEqual(bananaGrams.banana_grams(''), False)

    def test3(self):
        self.assertEqual(bananaGrams.banana_grams('bananaa'), False)

    def test4(self):
        self.assertEqual(bananaGrams.banana_grams('aaabnn'), True)

    def test5(self):
        self.assertEqual(bananaGrams.banana_grams('aaabn'), False)

    def test5(self):
        self.assertEqual(bananaGrams.banana_grams('asdhasd'), False)


if __name__ == '__main__':
    unittest.main()