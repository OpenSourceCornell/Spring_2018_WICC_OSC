import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import autograder

class autograderTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(autograder.autograder({"Homework": 50, "Prelim 1": 100, "Prelim 2": 100, "Final": 200, "Projects": 500, "Iclicker": 50}), 1000)
    
    def test2(self):
        self.assertEqual(autograder.autograder({"Homework": 0, "Prelim 1": 80, "Prelim 2": 90, "Final": 100, "Projects": 400, "Iclicker": 50}), 720)
    
    def test3(self):
        self.assertEqual(autograder.autograder({"Homework": 0, "Prelim 1": 0, "Prelim 2": 0, "Final": 0, "Projects": 0, "Iclicker": 14}), 14)

if __name__ == '__main__':
    unittest.main()