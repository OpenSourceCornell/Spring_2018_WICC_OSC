import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import addOpenSource

class AddOpenSourceTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(addOpenSource.add_open_source(['is','cool']), ['opensourceis','opensourcecool'])

    def test2(self):
        self.assertEqual(addOpenSource.add_open_source([]),[])

    def test3(self):
        self.assertEqual(addOpenSource.add_open_source(['opensource']),['opensourceopensource'])


if __name__ == '__main__':
    unittest.main()