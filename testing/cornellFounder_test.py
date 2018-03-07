import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import cornellFounder

class cornellFounderTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(cornellFounder.cornell_founder(), "Ezra Cornell")


if __name__ == '__main__':
    unittest.main()