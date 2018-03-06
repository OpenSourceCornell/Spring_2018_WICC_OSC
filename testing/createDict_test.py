import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import createDict

class createDictTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(createDict.create_dict('key', 'value'), {'key': 'value'})

    def test2(self):
        self.assertEqual(createDict.create_dict('a', 'b'), {'a': 'b'})

    def test2(self):
        self.assertEqual(createDict.create_dict('key', True), {'key': True})


if __name__ == '__main__':
    unittest.main()
