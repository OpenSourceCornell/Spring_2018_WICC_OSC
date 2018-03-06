import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import whereToEat

class whereToEatTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(whereToEat.where_to_eat('north'), 'RPCC')

    def test2(self):
        self.assertEqual(whereToEat.where_to_eat('west'),'Keeton' )

    def test2(self):
        self.assertEqual(whereToEat.where_to_eat('central'),'anywhere but Okenshields' )


if __name__ == '__main__':
    unittest.main()
