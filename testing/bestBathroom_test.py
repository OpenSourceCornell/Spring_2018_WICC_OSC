import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src/')
import bestBathroom

class bestBathroomTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(bestBathroom.best_bathroom(), "Gates Hall")

    def test2(self):
        self.assertEqual(bestBathroom.best_bathroom(), "Gates Hall")

    def test2(self):
        self.assertEqual(bestBathroom.best_bathroom(), "Gates Hall")


if __name__ == '__main__':
    unittest.main()
