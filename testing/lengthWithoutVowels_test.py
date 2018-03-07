import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import lengthWithoutVowels

class lengthWithoutVowelsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(lengthWithoutVowels.length_without_vowels('aeiou'), 0)

    def test2(self):
        self.assertEqual(lengthWithoutVowels.length_without_vowels('duffield'), 5)

    def test2(self):
        self.assertEqual(lengthWithoutVowels.length_without_vowels('nvwls'), 5)


if __name__ == '__main__':
    unittest.main()
