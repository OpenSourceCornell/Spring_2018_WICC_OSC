import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import sleepIn

class sleepInTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(sleepIn.sleep_in(True, True), True)

    def test2(self):
        self.assertEqual(sleepIn.sleep_in(True, False), True)

    def test3(self):
        self.assertEqual(sleepIn.sleep_in(False, False), False)

    def test4(self):
        self.assertEqual(sleepIn.sleep_in(False, True), True)


if __name__ == '__main__':
    unittest.main()